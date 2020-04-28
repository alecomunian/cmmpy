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
diagn["E-N-NE-SE"] = "18_E-N-NE-SE_noflow/out/diagn.csv"
diagn["E-N-SE-NE"] = "19_E-N-SE-NE_noflow/out/diagn.csv"
diagn["NE-SE-E-N"] = "20_NE-SE-E-N_noflow/out/diagn.csv"
diagn["E-NE-N-SE"] = "21_E-NE-N-SE_noflow/out/diagn.csv"

diagn["E-N-NE"]    = "22_E-N-NE_noflow/out/diagn.csv"
diagn["E-N"]       = "23_E-N_noflow/out/diagn.csv"
diagn["E"]         = "24_E_noflow/out/diagn.csv"
diagn["E-N-SE"]    = "25_E-N-SE_noflow/out/diagn.csv"
diagn["NE-SE"]     = "26_NE-SE_noflow/out/diagn.csv"
diagn["NE-SE-E"]   = "27_NE-SE-E_noflow/out/diagn.csv"
diagn["NE"]        = "28_NE_noflow/out/diagn.csv"
diagn["E-NE-N"]    = "29_E-NE-N_noflow/out/diagn.csv"
diagn["E-NE"]      = "30_E-NE_noflow/out/diagn.csv"

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

pl.savefig("dir_noflow__diagn.png", dpi=400)
pl.show()    
    

