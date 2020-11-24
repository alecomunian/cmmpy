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
import matplotlib.pylab as pl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import json
import sys

file_json = sys.argv[1]

# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)

lx = par["fwd"]["nx"]*par["fwd"]["dx"]
ly = par["fwd"]["ny"]*par["fwd"]["dy"]

it = 4
fixed_odg_T = 2

A = np.load("../out/test01_c/04_perc015/out/iter{0:03d}/ds000/A.npy".format(it))
err = np.load("../out/test01_c/04_perc015/out/test_Terr_iter{0:03d}.npy".format(it))

fig, ax = pl.subplots(1,2, sharey=True)


A_max = 0.1 #np.max(np.abs(A))


ax[0].set_title("a) $A_{{{0}}}$ (m)".format(it+1))

#im = ax[0].imshow(A[0,:,:], interpolation="none", cmap="PiYG", extent=(0.0,lx,0.0,ly ))
im = ax[0].imshow(A[0,:,:], interpolation="none", vmin=-A_max, vmax=A_max, cmap="PiYG", extent=(0.0,lx,0.0,ly ))

divider = make_axes_locatable(ax[0])
cax = divider.append_axes("right", size="5%", pad=0.05)
ax[0].set_xlabel("$x$ (m)")
ax[0].set_ylabel("$y$ (m)")
pl.colorbar(im, cax=cax)


vmin  = -fixed_odg_T
vmax  = fixed_odg_T

err_abs = np.abs(err)
ax[1].set_title("b) $\log(T^\mathrm{{(ref)}})-\log(T_\mathrm{{{0}}})$".format(it+1))
im = ax[1].imshow(err, vmin=vmin, vmax=vmax, interpolation="none",
                  cmap="Spectral", extent=(0.0,lx,0.0,ly ))
divider = make_axes_locatable(ax[1])
cax = divider.append_axes("right", size="5%", pad=0.05)
ax[1].set_xlabel("$x$ (m)")
#ax[1].set_ylabel("cells along $y$")
pl.colorbar(im, cax=cax)

pl.tight_layout()

pl.savefig("plot_A_e_err_perc15.png", dpi=400)
pl.savefig("plot_A_e_err_perc15.pdf")

