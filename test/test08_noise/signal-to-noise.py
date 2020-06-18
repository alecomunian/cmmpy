#!/usr/bin/env python3
"""
:This file:

    `script.py`

:Purpose:

    A sample script

:Usage:

    Explain here how to use it.

:Parameters:

:Version:

    0.1 , YYYY-MM-DD :

        * First version

:Authors:

    Alessandro Comunian

.. notes::

.. warning::

.. limitations::



"""
import matplotlib.pylab as pl
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import json
import sys
import flopy

file_h = []
# Read one head data set
file_h.append("../out/test08_noise/04_std10_S-SW-W-NW/out/ref/ds000/test.hds")
file_h.append("../out/test08_noise/04_std10_S-SW-W-NW/out/ref/ds001/test.hds")
file_h.append("../out/test08_noise/04_std10_S-SW-W-NW/out/ref/ds002/test.hds")
file_h.append("../out/test08_noise/04_std10_S-SW-W-NW/out/ref/ds003/test.hds")

head = []
for i in range(4):
    head.append(flopy.utils.HeadFile(file_h[i]).get_data())
    print(np.std(head[i]))
