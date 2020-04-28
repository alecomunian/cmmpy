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

import numpy as np
import pandas as pd
import matplotlib.pylab as pl

diagn = []



diagn.append({"file": "01_S/out/diagn.csv", "nbd": "S" })
diagn.append({"file": "02_S-SW/out/diagn.csv",  "nbd": "S, SW"})
diagn.append({"file": "03_S-SW-W/out/diagn.csv",  "nbd": "S, SW, W"})
diagn.append({"file": "04_S-SW-W-NW/out/diagn.csv",  "nbd": "S, SW, W, NW"})




for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}".format(dia["nbd"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("nbd_diagn.png", dpi=400)
pl.savefig("nbd_diagn.pdf")
pl.show()    
    

