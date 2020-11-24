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
import matplotlib.pylab as pl
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import json
import sys

file_json = sys.argv[1]

# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)

lx = par["fwd"]["nx"]*par["fwd"]["dx"]
ly = par["fwd"]["ny"]*par["fwd"]["dy"]

T={}



T["ref"] = np.load("../out/test10_md_natural/01_00/out/test_T_ref.npy")
T["01"] = np.load("../out/test10_md_natural/01_00/out/test_T_iter009.npy")
T["02"] = np.load("../out/test10_md_natural/02_00-10/out/test_T_iter009.npy")
T["03"] = np.load("../out/test10_md_natural/03_00-10-20/out/test_T_iter009.npy")
T["04"] = np.load("../out/test10_md_natural/04_00-10-20-30/out/test_T_iter009.npy")

t_min = np.min(T["ref"])
t_max = np.max(T["ref"])



fig, ax = pl.subplots(2,3, sharex=True, sharey=True, figsize=((8,4)))

coords = [(0,0),(0,1),(0,2),(1,1),(1,2)]
item = ["ref", "01", "02", "03", "04"]
xlab = [False, False, False,  True, True]
ylab = [True, False, False,  False, False]
titles = [
    "a) $T^\mathrm{ref}$",
    "b) $T_{10}$ - 0°",
    "c) $T_{10}$ - 0°, 10°",
    "d) $T_{10}$ - 0°, 10°, 20°",
    "e) $T_{10}$ - 0°, 10°, 20°, 30°"
    ]

for i in range(5):
    ax[coords[i]].set_title(titles[i])
    im = ax[coords[i]].imshow(T[item[i]][0,:,:], norm=LogNorm(vmin=t_min, vmax=t_max),
                        interpolation="none", cmap="inferno", extent=(0.0,lx,0.0,ly ))
#    divider = make_axes_locatable(ax[coords[i]])
#    cax = divider.append_axes("right", size="5%", pad=0.05)
#    ax[0,0].set_xlabel("$x$ (m)")
    if xlab[i]:
        ax[coords[i]].set_xlabel("$x$ (m)")
    if ylab[i]:
        ax[coords[i]].set_ylabel("$y$ (m)")
        
#    pl.colorbar(im, cax=cax)

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

# fig.text(0.5, 0.04, 'common X', ha='center')
# fig.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')

ax[1, 0].axis('off')


#pl.tight_layout()

pl.savefig("compare_T_dir", dpi=400)
pl.savefig("compare_T_dir.pdf")
