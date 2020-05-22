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



diagn.append({"file": "01_nbd04/out/diagn.csv", "nbd": 4 })
diagn.append({"file": "02_nbd03/out/diagn.csv",  "nbd": 3})
diagn.append({"file": "03_nbd02/out/diagn.csv",  "nbd": 2})
diagn.append({"file": "04_nbd01/out/diagn.csv",  "nbd": 1})




for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}".format(dia["nbd"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("nbd_diagn.png", dpi=400)
pl.show()    
    

