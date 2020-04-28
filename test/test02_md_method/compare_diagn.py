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



diagn.append({"file": "01_arith/out/diagn.csv", "meth": "arithmetic mean" })
diagn.append({"file": "02_geom/out/diagn.csv",  "meth": "geometric mean"})
diagn.append({"file": "03_harm/out/diagn.csv",  "meth": "harmonic mean"})
diagn.append({"file": "04_medi/out/diagn.csv",  "meth": "median"})
#diagn.append({"file": "05_mincX/out/diagn.csv",  "meth": "min.corr.X"})
diagn.append({"file": "05_darc/out/diagn.csv",  "meth": "Darcy residuals"})
diagn.append({"file": "06_minc/out/diagn.csv",  "meth": "minimum correction"})




for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}".format(dia["meth"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("meth_diagn.png", dpi=400)
pl.savefig("meth_diagn.pdf")
pl.show()    
    

