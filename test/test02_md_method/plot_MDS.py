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
import sklearn.manifold as sm

T = {}
T["ref"] = np.load("../out/test02_md_method/01_arith/out/test_T_ref.npy")
T["arith"] = np.load("../out/test02_md_method/01_arith/out/test_T_iter009.npy")
T["geom"] = np.load("../out/test02_md_method/02_geom/out/test_T_iter009.npy")
T["harm"] = np.load("../out/test02_md_method/03_harm/out/test_T_iter009.npy")
T["medi"] = np.load("../out/test02_md_method/04_medi/out/test_T_iter009.npy")
T["darc"] = np.load("../out/test02_md_method/05_darc/out/test_T_iter009.npy")
T["minc"] = np.load("../out/test02_md_method/06_minc/out/test_T_iter009.npy")

X = np.zeros((7,57*40))

X[0,:] = np.ravel(T["ref"])
X[1,:] = np.ravel(T["arith"])
X[2,:] = np.ravel(T["geom"])
X[3,:] = np.ravel(T["harm"])
X[4,:] = np.ravel(T["medi"])
X[5,:] = np.ravel(T["darc"])
X[6,:] = np.ravel(T["minc"])

labels = ["reference", "arithmetic", "geometric", "harmonic", "median", "Darcy", "min.corr."]

clf = sm.MDS(n_components=2, n_init=1, max_iter=1000)
X_mds = clf.fit_transform(X)

print(X_mds)

for i, label in enumerate(labels):
    pl.scatter(X_mds[i,0], X_mds[i,1], label=label)
pl.legend()    
pl.show()






