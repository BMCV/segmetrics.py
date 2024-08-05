.. raw:: html

  <div align="center">
    <h6>Image segmentation and object detection performance measures</h6>
    <h1>
      <a href="https://github.com/BMCV/segmetrics">segmetrics</a><br>
      <a href="https://github.com/BMCV/segmetrics/actions/workflows/testsuite.yml"><img src="https://github.com/BMCV/segmetrics/actions/workflows/testsuite.yml/badge.svg" /></a>
      <a href="https://github.com/BMCV/segmetrics/actions/workflows/testsuite.yml"><img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kostrykin/f46ddefff0798639bc320b13331dc7ca/raw/segmetrics.json" /></a>
      <a href="https://doi.org/10.5281/zenodo.10817137"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.10817137.svg" alt="DOI"></a><br>
      <a href="https://anaconda.org/bioconda/segmetrics"><img src="https://img.shields.io/badge/Install%20with-conda-%2387c305" /></a>
      <a href="https://anaconda.org/bioconda/segmetrics"><img src="https://img.shields.io/conda/v/bioconda/segmetrics.svg?label=Version" /></a>
      <a href="https://anaconda.org/bioconda/segmetrics"><img src="https://img.shields.io/conda/dn/bioconda/segmetrics.svg?label=Downloads" /></a>
      <a href="https://usegalaxy.eu/root?tool_id=toolshed.g2.bx.psu.edu/repos/imgteam/segmetrics/ip_segmetrics"><img src="https://img.shields.io/badge/usegalaxy-.eu-brightgreen?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAASCAYAAABB7B6eAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAAAsTAAALEwEAmpwYAAACC2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOlJlc29sdXRpb25Vbml0PjI8L3RpZmY6UmVzb2x1dGlvblVuaXQ+CiAgICAgICAgIDx0aWZmOkNvbXByZXNzaW9uPjE8L3RpZmY6Q29tcHJlc3Npb24+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlBob3RvbWV0cmljSW50ZXJwcmV0YXRpb24+MjwvdGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KD0UqkwAAAn9JREFUOBGlVEuLE0EQruqZiftwDz4QYT1IYM8eFkHFw/4HYX+GB3/B4l/YP+CP8OBNTwpCwFMQXAQPKtnsg5nJZpKdni6/6kzHvAYDFtRUT71f3UwAEbkLch9ogQxcBwRKMfAnM1/CBwgrbxkgPAYqlBOy1jfovlaPsEiWPROZmqmZKKzOYCJb/AbdYLso9/9B6GppBRqCrjSYYaquZq20EUKAzVpjo1FzWRDVrNay6C/HDxT92wXrAVCH3ASqq5VqEtv1WZ13Mdwf8LFyyKECNbgHHAObWhScf4Wnj9CbQpPzWYU3UFoX3qkhlG8AY2BTQt5/EA7qaEPQsgGLWied0A8VKrHAsCC1eJ6EFoUd1v6GoPOaRAtDPViUr/wPzkIFV9AaAZGtYB568VyJfijV+ZBzlVZJ3W7XHB2RESGe4opXIGzRTdjcAupOK09RA6kzr1NTrTj7V1ugM4VgPGWEw+e39CxO6JUw5XhhKihmaDacU2GiR0Ohcc4cZ+Kq3AjlEnEeRSazLs6/9b/kh4eTC+hngE3QQD7Yyclxsrf3cpxsPXn+cFdenF9aqlBXMXaDiEyfyfawBz2RqC/O9WF1ysacOpytlUSoqNrtfbS642+4D4CS9V3xb4u8P/ACI4O810efRu6KsC0QnjHJGaq4IOGUjWTo/YDZDB3xSIxcGyNlWcTucb4T3in/3IaueNrZyX0lGOrWndstOr+w21UlVFokILjJLFhPukbVY8OmwNQ3nZgNJNmKDccusSb4UIe+gtkI+9/bSLJDjqn763f5CQ5TLApmICkqwR0QnUPKZFIUnoozWcQuRbC0Km02knj0tPYx63furGs3x/iPnz83zJDVNtdP3QAAAABJRU5ErkJggg==" /></a>
    </h1>
  </div>

The goal of this package is to provide easy-to-use tools for evaluation of the performance of segmentation methods in biomedical image analysis and beyond, and to fasciliate the comparison of different methods by providing standardized implementations. This package currently only supports 2-D image data.

This tool is also available as a `web-app for the Galaxy platform`_.

.. _web-app for the Galaxy platform: https://usegalaxy.eu/root?tool_id=toolshed.g2.bx.psu.edu/repos/imgteam/segmetrics/ip_segmetrics

The documentation is available here: https://segmetrics.readthedocs.io

Use ``python -m unittest`` to run the test suite.

Contributions:
""""""""""""""

Contributions should be made against the ``develop`` branch, so that the documentation build on readthedocs.io is triggered, the documentation is built and reviewed (see `here <https://segmetrics.readthedocs.io/en/develop/>`_), before ``develop`` is merged into ``master``. This ensures that the ``master`` branch always has an up-to-date documentation.

----

.. raw:: html

  <div align="center">
    Copyright (c) 2017-2024 Leonid Kostrykin, Biomedical Computer Vision Group, Heidelberg University<br>
    This work is licensed under the terms of the MIT license. For a copy, see <a href="LICENSE">LICENSE</a>.
  </div>
