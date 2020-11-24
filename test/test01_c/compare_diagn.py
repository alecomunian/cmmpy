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



diagn.append({"file": "../out/test01_c/05_perc000/out/diagn.csv", "perc": 0})
diagn.append({"file": "../out/test01_c/04_perc015/out/diagn.csv", "perc": 15})
diagn.append({"file": "../out/test01_c/03_perc030/out/diagn.csv", "perc": 30})
diagn.append({"file": "../out/test01_c/02_perc060/out/diagn.csv", "perc": 60})
diagn.append({"file": "../out/test01_c/01_perc100/out/diagn.csv", "perc": 100})




for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}% data".format(dia["perc"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("compare_diagn_c.png", dpi=400)
pl.savefig("compare_diagn_c.pdf")
pl.show()    
    

