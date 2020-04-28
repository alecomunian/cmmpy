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


for i in range(8):
    diagn.append({"file": "{0:02d}_wells{1:02d}/out/diagn.csv".format(i+1, i+1), "wells": i+1})



#print(diagn)

for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}".format(dia["wells"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("wells_diagn.png", dpi=400)
pl.show()    
    

