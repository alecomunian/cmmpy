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
from matplotlib import rc
rc('text', usetex=True)

file_json = "04_00-10-20-30/test.json"
# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)


# The frequency of the flow lines


lx = par["fwd"]["nx"]*par["fwd"]["dx"]
ly = par["fwd"]["ny"]*par["fwd"]["dy"]

head_file1 = "../out/test10_md_natural/04_00-10-20-30/out/ref/ds000/test.hds"
head_file2 = "../out/test10_md_natural/04_00-10-20-30/out/ref/ds001/test.hds"
head_file3 = "../out/test10_md_natural/04_00-10-20-30/out/ref/ds002/test.hds"
head_file4 = "../out/test10_md_natural/04_00-10-20-30/out/ref/ds003/test.hds"
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

h_min = np.round(np.min(h), 2)
h_max = np.round(np.max(h), 2)
print(h_min, h_max)

levels = np.linspace(h_min, h_max, int((h_max-h_min)*2)+5)
print(levels)
ax[0,0].set_title("a) 0°")
cs = ax[0,0].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[0,0].clabel(cs, fmt="%.2f")
#ax[0,0].set_xlabel("$x$ (m)")
ax[0,0].set_ylabel("$y$ (m)")
#cax.remove()

h = head[1][0,:,:]

h_min = np.round(np.min(h), 2)
h_max = np.round(np.max(h), 2)

levels = np.linspace(h_min, h_max, int((h_max-h_min)*2)+5)
ax[0,1].set_title("b) 10°")
cs = ax[0,1].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[0,1].clabel(cs, fmt="%.2f")
#ax[0,1].set_xlabel("$x$ (m)")
#ax[0,1].set_ylabel("$y$ (m)")
#cax.remove()

h = head[2][0,:,:]

h_min = np.round(np.min(h), 2)
h_max = np.round(np.max(h), 2)

levels = np.linspace(h_min, h_max, int((h_max-h_min)*1)+5)
ax[1,0].set_title("c) 20°")
cs = ax[1,0].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
#divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[1,0].clabel(cs, fmt="%.2f")
ax[1,0].set_xlabel("$x$ (m)")
ax[1,0].set_ylabel("$y$ (m)")
#cax.remove()

h = head[3][0,:,:]

h_min = np.round(np.min(h),2)
h_max = np.round(np.max(h),2)

levels = np.linspace(h_min, h_max, int((h_max-h_min)*1)+5)
ax[1,1].set_title("d) 30°")
cs = ax[1,1].contour(np.flipud(h), levels=levels, extent=(0.0,lx,0.0,ly ))
#divider = make_axes_locatable(ax[0,1])
#cax = divider.append_axes("right", size="5%", pad=0.05)
ax[1,1].clabel(cs, fmt="%.2f")
ax[1,1].set_xlabel("$x$ (m)")
#ax[1,1].set_ylabel("$y$ (m)")
#cax.remove()

pl.tight_layout()
pl.savefig("hrefs.png", dpi=400)
pl.savefig("hrefs.pdf")


