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

# For the wells
diagnw = []


for i in range(8):
    diagnw.append({"file": "../out/test06_wells1a1/{0:02d}_wells{1:02d}/out/diagn.csv".format(i+1, i+1), "wells": i+1})
    
# For the direction
diagnd = []

diagnd.append({"file": "../out/test07_md_paper/01_S/out/diagn.csv", "nbd": "S" })
diagnd.append({"file": "../out/test07_md_paper/02_S-SW/out/diagn.csv",  "nbd": "S, SW"})
diagnd.append({"file": "../out/test07_md_paper/03_S-SW-W/out/diagn.csv",  "nbd": "S, SW, W"})
diagnd.append({"file": "../out/test07_md_paper/04_S-SW-W-NW/out/diagn.csv",  "nbd": "S, SW, W, NW"})


#fig, ax = pl.subplots(1,2)
fig, ax = pl.subplots(1,2,sharey=True,sharex=True,figsize=((8,4.5)))
for dia in diagnd:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    ax[0].plot(it, data["lmbd2"], "-o", label="{0}".format(dia["nbd"]))

ax[0].set_xlabel("iteration")
ax[0].set_title("a) $\lambda^2$ - flow direction")
x0a, x1a = ax[0].get_xlim()
y0a, y1a = ax[0].get_ylim()
print(y0a, y1a)
ax[0].legend()


for dia in diagnw:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    ax[1].plot(it, data["lmbd2"], "-o", label="{0}".format(dia["wells"]))

ax[1].set_xlabel("iteration")
ax[1].set_title("b) $\lambda^2$ - wells number")
x0b, x1b = ax[1].get_xlim()
print(x0b, x1b)
y0b, y1b = ax[1].get_ylim()
print(y0b,y1b)

ax[1].legend()

# x1 = np.maximum(x1a,x1b)
# x0 = np.minimum(x0a,x0b)
# y1 = np.maximum(y1a,y1b)
# y0 = np.minimum(y0a,y0b)

x1 = np.minimum(x1a,x1b)
x0 = np.maximum(x0a,x0b)
y1 = np.minimum(y1a,y1b)
y0 = np.maximum(y0a,y0b)


# print(x1, x0, y1, y0)
# ax[0].set_aspect((x1-x0/(y1-y0)))

# ax[1].set_aspect((np.maximum(x1a,x1b)-np.minimum(x0a,x0b)/(np.maximum(y1a,y1b)-np.minimum(y0a,y0b))))



pl.tight_layout()

pl.savefig("diagn_dir-and-wells.png", dpi=400)
pl.savefig("diagn_dir-and-wells.pdf")
pl.show()    
    

