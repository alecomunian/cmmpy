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
import flopy
import matplotlib.pylab as pl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import json

file_json = "01_arith/test.json"
# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)


# The frequency of the flow lines


lx = par["fwd"]["nx"]*par["fwd"]["dx"]
ly = par["fwd"]["ny"]*par["fwd"]["dy"]

head_file1 = "../out/test02_md_method/01_arith/out/ref/ds000/test.hds"
head_file2 = "../out/test02_md_method/01_arith/out/ref/ds001/test.hds"
head_file3 = "../out/test02_md_method/01_arith/out/ref/ds002/test.hds"
head_file4 = "../out/test02_md_method/01_arith/out/ref/ds003/test.hds"
#bud_file1 = "01_arith/out/ref/ds000/test.bud"

head = {}
bud = {}
head[0] = flopy.utils.HeadFile(head_file1).get_data()
head[1] = flopy.utils.HeadFile(head_file2).get_data()
head[2] = flopy.utils.HeadFile(head_file3).get_data()
head[3] = flopy.utils.HeadFile(head_file4).get_data()
#bud[0] = flopy.utils.CellBudgetFile(bud_file1, precision='double')


fig, ax = pl.subplots(2,2, sharex=True, sharey=True)

# h = head[0][0,:,:]
# ax[0,0].set_title("a)")
# ax[0,0].imshow(head[0][0,:,:])


h = head[0][0,:,:]

h_min = np.floor(np.min(h))
h_max = np.floor(np.max(h))

levels = np.linspace(h_min, h_max, int((h_max-h_min)*2)+5)
ax[0,0].set_title("a) south (S)")
cs = ax[0,0].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[0,0].clabel(cs, fmt="%.2f")
#ax[0,0].set_xlabel("$x$ ($\si{m}$)")
ax[0,0].set_ylabel("$y$ ($\si{m}$)")
#cax.remove()

h = head[1][0,:,:]

h_min = np.floor(np.min(h))
h_max = np.floor(np.max(h))

levels = np.linspace(h_min, h_max, int((h_max-h_min)*2)+5)
ax[0,1].set_title("b) west (W)")
cs = ax[0,1].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[0,1].clabel(cs, fmt="%.2f")
#ax[0,1].set_xlabel("$x$ ($\si{m}$)")
#ax[0,1].set_ylabel("$y$ ($\si{m}$)")
#cax.remove()

h = head[2][0,:,:]

h_min = np.floor(np.min(h))
h_max = np.floor(np.max(h))

levels = np.linspace(h_min, h_max, int((h_max-h_min)*1)+5)
ax[1,0].set_title("c) south-west (SW)")
cs = ax[1,0].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
#divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[1,0].clabel(cs, fmt="%.2f")
ax[1,0].set_xlabel("$x$ ($\si{m}$)")
ax[1,0].set_ylabel("$y$ ($\si{m}$)")
#cax.remove()

h = head[3][0,:,:]

h_min = np.floor(np.min(h))
h_max = np.floor(np.max(h))

levels = np.linspace(h_min, h_max, int((h_max-h_min)*1)+5)
ax[1,1].set_title("d) north-west (NW)")
cs = ax[1,1].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
#divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[1,1].clabel(cs, fmt="%.2f")
ax[1,1].set_xlabel("$x$ ($\si{m}$)")
#ax[1,1].set_ylabel("$y$ ($\si{m}$)")
#cax.remove()

pl.tight_layout()
pl.savefig("hrefs.png", dpi=400)
pl.savefig("hrefs.pdf")


