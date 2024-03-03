from scipy import ndimage

from segmetrics._aux import bbox


class Measure:
    """
    Defines a performance measure.

    :param aggregation:
        Indicates whether the results of this performance measure are
        aggregated by summation (``sum``), by averaging (``mean``), or by
        computing the proportion with respect to the number of annotated
        objects (``obj-mean``).
    """

    def __init__(self, aggregation='mean'):
        self.aggregation = aggregation

    def set_expected(self, expected):
        """
        Sets the expected result for evaluation.

        :param expected:
            An image containing uniquely labeled object masks corresponding to
            the ground truth.
        """
        self.expected = expected

    def compute(self, actual):
        """
        Computes the performance measure for the given segmentation results
        based on the previously set expected result.

        :param actual:
            An image containing uniquely labeled object masks corresponding to
            the segmentation results.
        """
        return NotImplemented

    def default_name(self):
        """
        Returns the default name of this measure.
        """
        return type(self).__name__


class ImageMeasure(Measure):
    """
    Defines an image-level performance measure.

    The computation of such measures only regards the union of the individual
    objects, not the individual objects themselves.

    :param correspondance_function:
        Determines how the object correspondances are determined when using
        the :meth:`object_based` method. Must be either ``min`` (use the
        object with the minimal score) or ``max`` (use the object with the
        maximal score).
    """

    def __init__(self, correspondance_function):
        assert correspondance_function in (
            'min',
            'max',
        )
        self.correspondance_function = correspondance_function

    def object_based(self, *args, **kwargs):
        """
        Returns measure for comparison regarding the individual objects (as
        opposed to only considering their union).

        Positional and keyword arguments are passed through to
        :class:`ObjectMeasureAdapter`.

        :returns:
            This measure decorated by :class:`ObjectMeasureAdapter`.
        """
        return ObjectMeasureAdapter(
            self,
            *args,
            correspondance_function={
                'min': min,
                'max': max,
            }[self.correspondance_function],
            **kwargs
        )


class ObjectMeasureAdapter(Measure):
    """
    Adapter to use image-level measures on a per-object level.

    Computes the underlying image-level measure on a per-object level. Object
    correspondances between the segmented and the ground truth objects are
    established on a many-to-many basis, so that the resulting scores are
    either minimal or maximal.

    :param measure:
        The underlying image-level measure.

    :param correspondance_function:
        Determines the object correspondances by reducing a sequence of scores
        to a single score value.
    """

    _obj_mapping = (None, None)  # cache

    def __init__(self, measure, correspondance_function):
        super().__init__()
        self.measure      = measure
        self.aggregation  = measure.aggregation
        self.nodetections = -1  # value to be used if detections are empty
        self.correspondance_function = correspondance_function

    def set_expected(self, *args, **kwargs):
        super().set_expected(*args, **kwargs)
        ObjectMeasureAdapter._obj_mapping = (None, dict())

    def compute(self, actual):
        results = []
        seg_labels = frozenset(actual.reshape(-1)) - {0}

        # Reset the cached object mapping:
        if ObjectMeasureAdapter._obj_mapping[0] is not actual:
            ObjectMeasureAdapter._obj_mapping = (actual, dict())

        for ref_label in set(self.expected.flatten()) - {0}:
            ref_cc = (self.expected == ref_label)

            # If there were no detections, then there are no correspondances,
            # and thus no object-level scores can be determined:
            if len(seg_labels) == 0:
                if self.nodetections >= 0:
                    results.append(self.nodetections)
                continue

            # Query the cached object mapping:
            if ref_label in self._obj_mapping[1]:  # cache hit

                potentially_closest_seg_labels = \
                    ObjectMeasureAdapter._obj_mapping[1][ref_label]

            else:  # cache miss

                # First, narrow the set of potentially corresponding objects
                # by determining the labels of objects with non-empty overlap:
                ref_distancemap = ndimage.distance_transform_edt(~ref_cc)
                closest_potential_seg_label = min(
                    seg_labels,
                    key=lambda seg_label: ref_distancemap[
                            actual == seg_label
                        ].min(),
                )
                max_potential_seg_label_distance = ref_distancemap[
                    actual == closest_potential_seg_label
                ].max()
                potentially_closest_seg_labels = [
                    seg_label for seg_label in seg_labels
                    if ref_distancemap[
                        actual == seg_label
                    ].min() <= max_potential_seg_label_distance
                ]
                ObjectMeasureAdapter._obj_mapping[1][
                    ref_label
                ] = potentially_closest_seg_labels

            # If not a single object was detected, the distance is undefined:
            if len(potentially_closest_seg_labels) == 0:
                continue

            distances = []
            for seg_label in potentially_closest_seg_labels:
                seg_cc = (actual == seg_label)
                _bbox  = bbox(ref_cc, seg_cc, margin=1)[0]
                self.distance.set_expected(ref_cc[_bbox].astype('uint8'))
                distance = self.distance.compute(seg_cc[_bbox].astype('uint8'))
                assert len(distance) == 1
                distances.append(distance[0])
            results.append(self.correspondance_function(distances))
        return results

    def default_name(self):
        name = f'Ob. {self.distance.default_name()}'
        if self.skip_fn:
            skip_fn_hint = f'skip_fn={self.skip_fn}'
            if name.endswith(')'):
                name = name[:-1] + f', {skip_fn_hint})'
            else:
                name += f' ({skip_fn_hint})'
        return name
