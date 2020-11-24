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
from matplotlib.colors import LogNorm
import json
import sys
import os 

file_json = "all_wells/test.json"
data_path = "../data/bcs_rect.txt"
t_file = "../out/test01_c/01_perc100/out/test_T_ref.npy"
ds = 0

# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)

lx = par["fwd"]["nx"]*par["fwd"]["dx"]
ly = par["fwd"]["ny"]*par["fwd"]["dy"]
dx = par["fwd"]["dx"]
dy = par["fwd"]["dy"]

T = np.load(t_file)


# Read an external file containing the shape of the domain
bcs = np.fliplr(np.transpose(np.loadtxt(data_path,
                                        dtype="U1")))
domain = np.zeros(bcs.shape)
domain[bcs=="E"] = 1 # External cells
domain[bcs=="D"] = 2 # Dirichlet BCs
domain[bcs=="I"] = 3 # Internal cells

fig, ax = pl.subplots(1,2, sharey=True)

ax[0].set_title("a) Domain geometry")
ax[0].set_xlabel("$x$ (m)")
ax[0].set_ylabel("$y$ (m)")
cmap = pl.cm.get_cmap('Accent', 3)
im = ax[0].imshow(np.transpose(domain), cmap=cmap, vmin=1, vmax=3, extent=(0.0,lx,0.0,ly ))
if ds is not None:
    # Plot domain is used to plot data for a specific data set,
    # therefore well locations should be included
    for i, well in enumerate(par["fwd"]["data_sets"][ds]["wells_ID"]):
        y, x = par["fwd"]["data_sets"][ds]["wells_loc"][i][1:]
        ax[0].scatter(x*dx,ly-y*dy, marker="x", c="yellow")
        ax[0].text(x*dx+25,ly-y*dy+25, par["fwd"]["data_sets"][ds]["wells_ID"][i], color="yellow")
        
ax[0].text(150, 800, "N", color="yellow", horizontalalignment='center', fontweight="bold")
ax[0].arrow( 150, 600, 0.0, 150, fc="yellow", ec="yellow", head_width=20, head_length=20, lw=3 )


divider = make_axes_locatable(ax[0])
cax = divider.append_axes("right", size="5%", pad=0.05)
cbar = pl.colorbar(im, cax=cax)
cbar = pl.colorbar(im, cax=cax, ticks=[1.33, 2, 2.66])    
cbar.ax.set_yticklabels(['E', 'D', 'I'])

t_min = np.min(T)
t_max = np.max(T)

ax[1].set_title("b) $T^\mathrm{(ref)}$ ($\mathrm{m^2/s}$)")
im = ax[1].imshow(T[0,:,:], norm=LogNorm(vmin=t_min, vmax=t_max),
               interpolation="none", cmap="inferno", extent=(0.0,lx,0.0,ly ))
divider = make_axes_locatable(ax[1])
cax = divider.append_axes("right", size="5%", pad=0.05)
ax[1].set_xlabel("$x$ (m)")
#ax[1].set_ylabel("ells along $y$")
pl.colorbar(im, cax=cax)

pl.tight_layout()

pl.savefig("domain_and_Tref.png", dpi=400)
pl.savefig("domain_and_Tref.pdf")

