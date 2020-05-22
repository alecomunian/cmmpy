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

def plotta(dire, diagn, ax):
    data = pd.read_csv(diagn[dire])
    it = np.arange(1, data["lmbd2"].size+1)
    ax.plot(it, data["lmbd2"], "-o", label="{0}".format(dire))
    ax.legend()
    

diagn = {}
diagn["E-N-NE-SE"] = "05_E-N-NE-SE/out/diagn.csv"
diagn["E-N-SE-NE"] = "06_E-N-SE-NE/out/diagn.csv"
diagn["NE-SE-E-N"] = "07_NE-SE-E-N/out/diagn.csv"
diagn["E-NE-N-SE"] = "08_E-NE-N-SE/out/diagn.csv"

diagn["E-N-NE"]    = "09_E-N-NE/out/diagn.csv"
diagn["E-N"]       = "10_E-N/out/diagn.csv"
diagn["E"]         = "11_E/out/diagn.csv"
diagn["E-N-SE"]    = "12_E-N-SE/out/diagn.csv"
diagn["NE-SE"]     = "13_NE-SE/out/diagn.csv"
diagn["NE-SE-E"]   = "14_NE-SE-E/out/diagn.csv"
diagn["NE"]        = "15_NE/out/diagn.csv"
diagn["E-NE-N"]    = "16_E-NE-N/out/diagn.csv"
diagn["E-NE"]      = "17_E-NE/out/diagn.csv"

fig, ax = pl.subplots(2,2, sharex=True, sharey=True)
plotta("E", diagn, ax[0,0])
plotta("E-N", diagn, ax[0,0])
plotta("E-N-NE", diagn, ax[0,0])
plotta("E-N-NE-SE", diagn, ax[0,0])



ax[0,0].set_title("a)")
ax[0,0].set_ylim((0.0, 0.35))

plotta("E", diagn, ax[0,1])
plotta("E-N", diagn, ax[0,1])
plotta("E-N-SE", diagn, ax[0,1])
plotta("E-N-SE-NE", diagn, ax[0,1])



ax[0,1].set_title("b)")

plotta("NE", diagn, ax[1,0])
plotta("NE-SE", diagn, ax[1,0])
plotta("NE-SE-E", diagn, ax[1,0])
plotta("NE-SE-E-N", diagn, ax[1,0])



ax[1,0].set_title("c)")

plotta("E", diagn, ax[1,1])
plotta("E-NE", diagn, ax[1,1])
plotta("E-NE-N", diagn, ax[1,1])
plotta("E-NE-N-SE", diagn, ax[1,1])



ax[1,1].set_title("d)")







ax[1,0].set_xlabel("iteration")
ax[1,1].set_xlabel("iteration")
ax[1,0].set_ylabel("$\lambda^2$")
ax[0,0].set_ylabel("$\lambda^2$")    
pl.tight_layout()

pl.savefig("dir_diagn.png", dpi=400)
pl.show()    
    

