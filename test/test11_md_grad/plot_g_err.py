#!/usr/bin/env python3
"""
:This file:

    `plot_g_rel.py`

:Purpose:

    Plot the relative error on the gradient

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

g_rel1 = []
g_rel1.append(np.load("../out/test11_md_grad/01_00-10-20-30_gr0d001_std00/out/g_rel.npy"))
g_rel1.append(np.load("../out/test11_md_grad/02_00-10-20-30_gr0d001_std05/out/g_rel.npy"))
g_rel1.append(np.load("../out/test11_md_grad/03_00-10-20-30_gr0d001_std10/out/g_rel.npy"))
g_rel1.append(np.load("../out/test11_md_grad/04_00-10-20-30_gr0d001_std20/out/g_rel.npy"))

g_rel2 = []
g_rel2.append(np.load("../out/test11_md_grad/05_00-10-20-30_gr0d002_std00/out/g_rel.npy"))
g_rel2.append(np.load("../out/test11_md_grad/06_00-10-20-30_gr0d002_std05/out/g_rel.npy"))
g_rel2.append(np.load("../out/test11_md_grad/07_00-10-20-30_gr0d002_std10/out/g_rel.npy"))
g_rel2.append(np.load("../out/test11_md_grad/08_00-10-20-30_gr0d002_std20/out/g_rel.npy"))



nb_xx, nb_row, nb_col, nb_iter, nb_ds = g_rel1[0].shape


nb_gra = 2
nb_std = 4
wisk = np.zeros((nb_row*nb_col, nb_iter, nb_ds, nb_gra, nb_std))

# Selected data-set

sel_ds = 3

fig, ax = pl.subplots(4,2, sharex=True, sharey=False)

lab_gra1 = ["a) grad 0.001, std 0 cm",
            "c) grad 0.001, std 5 cm",
            "e) grad 0.001, std 10 cm",
            "g) grad 0.001, std 20 cm"]

lab_gra2 = ["b) grad 0.002, std 0 cm",
            "d) grad 0.002, std 5 cm",
            "f) grad 0.002, std 10 cm",
            "h) grad 0.002, std 20 cm"]

lab_gra = [lab_gra1, lab_gra2]

#wisk = []
for i in range(nb_iter):
    for j in range(nb_std):
        wisk[:,i,sel_ds,0,j] = np.ravel(g_rel1[j][0,:,:,i,sel_ds])
        wisk[:,i,sel_ds,1,j] = np.ravel(g_rel2[j][0,:,:,i,sel_ds])

for row in range(4):
    for col in range(2):
        ax[row, col].boxplot(wisk[:,:,sel_ds,col,row], whis=(0,100))
        ax[row, col].set_title(lab_gra[col][row])
#        ax[row, col].set_yscale('log')
#        ax[row, col].set_ylim((0, 20))

# wisk = []
# for i in range(nb_iter):
#     wisk.append(np.ravel(g_rel1[1][0,:,:,i,sel_ds]))        
# ax[1,0].boxplot(wisk, whis=(0,100))

# wisk = []
# for i in range(nb_iter):
#     wisk.append(np.ravel(g_rel1[2][0,:,:,i,sel_ds]))        
# ax[2,0].boxplot(wisk, whis=(0,100))

# wisk = []
# for i in range(nb_iter):
#     wisk.append(np.ravel(g_rel1[3][0,:,:,i,sel_ds]))        
# ax[3,0].boxplot(wisk, whis=(0,100))


pl.tight_layout()
pl.savefig("g_rel.pdf")
pl.show()
