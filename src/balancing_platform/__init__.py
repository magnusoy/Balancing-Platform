# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences


from pkg_resources import get_distribution, DistributionNotFound
import cv2
import numpy
import pymodbus
import vpython
import matplotlib

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __all__ = [cv2, numpy, pymodbus, vpython, matplotlib]
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = '1.0'
