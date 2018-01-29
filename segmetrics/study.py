import skimage.measure
import numpy as np


def _is_boolean(narray):
    return narray.dtype == np.bool

def _is_integral(narray):
    return issubclass(narray.dtype.type, np.integer)

def _get_labeled(narray, unique, img_hint):
    assert _is_integral(narray) or _is_boolean(narray), 'illegal %s dtype' % img_hint
    assert not unique or not _is_boolean(narray), 'with unique=True a non-boolean %s is expected' % img_hint
    return narray if unique else label(narray)

def _get_skimage_measure_label_bg_label():
    """Determines the background label generated by the `label` routine of `skimage.measure`.

    The value of the background label varies from version to version.
    """
    return skimage.measure.label(np.array([[1, 0]]), background=0).min()

_SKIMAGE_MEASURE_LABEL_BF_LABEL = _get_skimage_measure_label_bg_label()

def label(im, background=0, neighbors=4):
    """Labels the given image `im`.
    
    Returns a labeled version of `im` where `background` is labeled with
    0 and all other connected components are labeled with values larger
    than or equal to 1.
    """
    return skimage.measure.label(im, background=background, neighbors=neighbors) \
        - _SKIMAGE_MEASURE_LABEL_BF_LABEL # this is 1 in older versions and 0 in newer


class Study:

    def __init__(self):
        self.measures = {}
        self.results  = {}

    def add_measure(self, measure, name=None):
        if name is None: name = '%d' % id(measure)
        self.measures[name] = measure
        self.results [name] = []

    def set_expected(self, expected, unique=True):
        """Sets the `expected` ground truth image.
        
        The background must be labeled as 0. Negative object labels are
        forbidden. If `unique` is `True`, it is assumed that all objects
        are labeled uniquely. Set it to `False`, if this is not sure
        (e.g., if the ground truth image is binary).

        The array `expected` must be of integral datatype. It is also
        allowed to be boolean if and only if `unique=False` is passed.
        """
        assert expected.min() == 0, 'mis-labeled ground truth'
        expected = expected.squeeze()
        assert expected.ndim == 2, 'ground truth has wrong dimensions'
        expected = _get_labeled(expected, unique, 'ground truth')
        for measure_name in self.measures:
            measure = self.measures[measure_name]
            measure.set_expected(expected)

    def process(self, actual, unique=True):
        """Evaluates `actual` image against the current `set_expected` one.
        
        If `unique` is `True`, it is assumed that all objects are labeled
        uniquely. Set it to `False`, if this is not sure (e.g., if the
        processed image is binary).

        The array `actual` must be of integral datatype. It is also
        allowed to be boolean if and only if `unique=False` is passed.
        """
        actual = actual.squeeze()
        assert actual.ndim == 2, 'image has wrong dimensions'
        actual = _get_labeled(actual, unique, 'image')
        intermediate_results = {}
        for measure_name in self.measures:
            measure = self.measures[measure_name]
            result = measure.compute(actual)
            self.results[measure_name] += result
            intermediate_results[measure_name] = result
        return intermediate_results

