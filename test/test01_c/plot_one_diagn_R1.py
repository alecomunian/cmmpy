#!/usr/bin/env python3
"""
:This file:

    `plot_one_diagn_R1.py`

:Purpose:

    Plot some diagnostic results

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



dia = {"file": "../out/test01_c/04_perc015/out/diagn.csv"}


#fig, ax = pl.subplots(1,4)
fig, ax = pl.subplots(1,3, figsize=(6,3))

data = pd.read_csv(dia["file"])
it = np.arange(1, data["lmbd2"].size+1)





ax[0].set_xlabel("iteration")
ax[0].set_title("a) $\lambda$")    
ax[0].plot(it, data["lmbd"], "-o")
x0, x1 = ax[0].get_xlim()
y0, y1 = ax[0].get_ylim()
ax[0].set_aspect((x1-x0)/(y1-y0))

# ax[1].set_xlabel("iteration")
# ax[1].set_title("b) $|\lambda|$")    
# ax[1].plot(it, data["lmbd_abs"], "-o")
# x0, x1 = ax[1].get_xlim()
# y0, y1 = ax[1].get_ylim()
# ax[1].set_aspect((x1-x0)/(y1-y0))


ax[1].set_xlabel("iteration")
ax[1].set_title("b) $\lambda^2$")    
ax[1].plot(it, data["lmbd2"], "-o")
x0, x1 = ax[1].get_xlim()
y0, y1 = ax[1].get_ylim()
ax[1].set_aspect((x1-x0)/(y1-y0))

nb_ds = len(data.keys())-3
for i in range(nb_ds):
    ax[2].plot(it, data["a{0}".format(i)], "-o")
ax[2].set_xlabel("iteration")
ax[2].set_title("c) mean $|A|$ (m)")
x0, x1 = ax[2].get_xlim()
y0, y1 = ax[2].get_ylim()
ax[2].set_aspect((x1-x0)/(y1-y0))

pl.tight_layout()
pl.savefig("c_diagn_perc15_R1.png", dpi=400)
pl.savefig("c_diagn_perc15_R1.pdf")
#pl.show()    
    

