#!/usr/bin/env python3
"""
:This file:

    `compare_diagn4paper.py`

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
from matplotlib.lines import Line2D


prop_cycle = pl.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


diagn1 = []
diagn2 = []
diagn3 = []


# Plotted with "-"
diagn1.append({"file": "../out/test12_md_grad_unstr/01_00-10-20-30_gr0d001_std00/out/diagn.csv", "nbd": "0.001, 0" })
diagn1.append({"file": "../out/test12_md_grad_unstr/02_00-10-20-30_gr0d001_std05/out/diagn.csv",  "nbd": "0.001, 5"})
diagn1.append({"file": "../out/test12_md_grad_unstr/03_00-10-20-30_gr0d001_std10/out/diagn.csv",  "nbd": "0.001, 10"})
diagn1.append({"file": "../out/test12_md_grad_unstr/04_00-10-20-30_gr0d001_std20/out/diagn.csv",  "nbd": "0.001, 20"})


# Plotted with ":"

diagn2.append({"file": "../out/test12_md_grad_unstr/05_00-10-20-30_gr0d002_std00/out/diagn.csv",  "nbd": "0 cm"})
diagn2.append({"file": "../out/test12_md_grad_unstr/06_00-10-20-30_gr0d002_std05/out/diagn.csv",  "nbd": "5 cm"})
diagn2.append({"file": "../out/test12_md_grad_unstr/07_00-10-20-30_gr0d002_std10/out/diagn.csv",  "nbd": "10 cm"})
diagn2.append({"file": "../out/test12_md_grad_unstr/08_00-10-20-30_gr0d002_std20/out/diagn.csv",  "nbd": "20 cm"})


diagn3.append({"file": "../out/test12_md_grad_unstr/09_00-10-20-30_gr0d0015_std00/out/diagn.csv",  "nbd": "0 cm"})
diagn3.append({"file": "../out/test12_md_grad_unstr/10_00-10-20-30_gr0d0015_std05/out/diagn.csv",  "nbd": "5 cm"})
diagn3.append({"file": "../out/test12_md_grad_unstr/11_00-10-20-30_gr0d0015_std10/out/diagn.csv",  "nbd": "10 cm"})
diagn3.append({"file": "../out/test12_md_grad_unstr/12_00-10-20-30_gr0d0015_std20/out/diagn.csv",  "nbd": "20 cm"})

# diagn2.append({"file": "../out/test12_md_grad_unstr/05_00-10-20-30_gr0d002_std00/out/diagn.csv",  "nbd": "0.002 0"})
# diagn2.append({"file": "../out/test12_md_grad_unstr/06_00-10-20-30_gr0d002_std05/out/diagn.csv",  "nbd": "0.002 05"})
# diagn2.append({"file": "../out/test12_md_grad_unstr/07_00-10-20-30_gr0d002_std10/out/diagn.csv",  "nbd": "0.002 10"})
# diagn2.append({"file": "../out/test12_md_grad_unstr/08_00-10-20-30_gr0d002_std20/out/diagn.csv",  "nbd": "0.002 20"})


fig, ax = pl.subplots(1,2,sharex=True, figsize=(10,4))


for i, dia in enumerate(diagn1):
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    ax[0].plot(it, data["lmbd2"], "-x", c=colors[i])
    ax[1].plot(it, data["a0"], "-x", c=colors[i])
#    pl.plot(it, data["lmbd2"], ":v", label="{0}".format(dia["nbd"]))   


for i, dia in enumerate(diagn2):
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    ax[0].plot(it, data["lmbd2"], "-o", c=colors[i], markerfacecolor="none")
    ax[1].plot(it, data["a0"], "-o", c=colors[i], markerfacecolor="none")


# for dia in diagn3:
#     data = pd.read_csv(dia["file"])
#     it = np.arange(1, data["lmbd2"].size+1)
#     pl.plot(it, data["lmbd2"], ":+", markerfacecolor="none")

# pl.gca().set_prop_cycle(None)


    
ax[0].set_xlabel("iteration")
ax[1].set_xlabel("iteration")
ax[0].set_title("a) $\lambda^2$")
ax[1].set_title("b) MAE on $h$")


custom_lines = [Line2D([0], [0], color=colors[0]),
                Line2D([0], [0], color=colors[1]),
                Line2D([0], [0], color=colors[2]),
                Line2D([0], [0], color=colors[3])]


ax[0].legend(custom_lines, ("0 cm", "5 cm", "10 cm", "20 cm"))


pl.savefig("nbd_diagn4paper_unstr.png", dpi=400)
pl.savefig("nbd_diagn4paper_unstr.pdf")
pl.show()    
    

