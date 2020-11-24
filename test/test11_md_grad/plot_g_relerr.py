#!/usr/bin/env python3
"""
:This file:

    `plot_g_relerr.py`

:Purpose:

    Plot the relative error on the starting gradients affected by
    different noise...

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

sel_ds = 3

file1_std00 = "../out/test11_md_grad/01_00-10-20-30_gr0d001_std00/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)
file1_std05 = "../out/test11_md_grad/02_00-10-20-30_gr0d001_std05/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)
file1_std10 = "../out/test11_md_grad/03_00-10-20-30_gr0d001_std10/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)
file1_std20 = "../out/test11_md_grad/04_00-10-20-30_gr0d001_std20/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)

file2_std00 = "../out/test11_md_grad/05_00-10-20-30_gr0d002_std00/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)
file2_std05 = "../out/test11_md_grad/06_00-10-20-30_gr0d002_std05/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)
file2_std10 = "../out/test11_md_grad/07_00-10-20-30_gr0d002_std10/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)
file2_std20 = "../out/test11_md_grad/08_00-10-20-30_gr0d002_std20/out/ref/ds00{0:1d}/h.vtk".format(sel_ds)


data1 = {}

data1["00"] = np.reshape(np.loadtxt(file1_std00, skiprows=10), (40,57))
data1["05"] = np.reshape(np.loadtxt(file1_std05, skiprows=10), (40,57))
data1["10"] = np.reshape(np.loadtxt(file1_std10, skiprows=10), (40,57))
data1["20"] = np.reshape(np.loadtxt(file1_std20, skiprows=10), (40,57))


data2 = {}

data2["00"] = np.reshape(np.loadtxt(file2_std00, skiprows=10), (40,57))
data2["05"] = np.reshape(np.loadtxt(file2_std05, skiprows=10), (40,57))
data2["10"] = np.reshape(np.loadtxt(file2_std10, skiprows=10), (40,57))
data2["20"] = np.reshape(np.loadtxt(file2_std20, skiprows=10), (40,57))


grad1i = {}
grad1j = {}
grad2i = {}
grad2j = {}

for std in ["00", "05", "10", "20"]:
    grad1i[std], grad1j[std] = np.gradient(data1[std])
    grad2i[std], grad2j[std] = np.gradient(data2[std])


erel1 = {}
erel2 = {}
e1x = []
e1y = []
e2x = []
e2y = []
e1 = []
e2 = []
for std in ["05", "10", "20"]:
    erel1i = (grad1i[std]-grad1i["00"]) / grad1i["00"]
    erel1j = (grad1j[std]-grad1j["00"]) / grad1j["00"]
    erel2i = (grad2i[std]-grad2i["00"]) / grad2i["00"]
    erel2j = (grad2j[std]-grad2j["00"]) / grad2j["00"]

    erel1[std] = np.hypot(erel1i, erel1j)
    erel2[std] = np.hypot(erel2i, erel2j)

    e1x.append(np.ravel(erel1j))
    e1y.append(np.ravel(erel1i))
    e2x.append(np.ravel(erel2j))
    e2y.append(np.ravel(erel2i))
    e1.append(np.ravel(erel1[std]))
    e2.append(np.ravel(erel2[std]))
    
# fig, ax = pl.subplots(3,2)

# for i, std in enumerate(["05", "10", "20"]):
#     im = ax[i,0].imshow(erel1[std])
#     fig.colorbar(im, ax=ax[i,0])
#     im = ax[i,1].imshow(erel2[std])
#     fig.colorbar(im, ax=ax[i,1])


# pl.show()

fig, ax = pl.subplots(2,3)

ax[0,0].boxplot(e1x, whis=(0,100))
#ax[0,0].set_ylim((-1,1))
ax[0,1].boxplot(e1y, whis=(0,100))
ax[0,2].boxplot(e1, whis=(0,100))
ax[1,0].boxplot(e2x, whis=(0,100))
ax[1,1].boxplot(e2y, whis=(0,100))
ax[1,2].boxplot(e2, whis=(0,100))



pl.show()



    




