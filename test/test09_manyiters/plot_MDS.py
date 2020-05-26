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



tot_iter = 80


X = np.zeros((tot_iter+1,57*40))

for i in range(tot_iter):
    X[i,:] = np.ravel(np.load("../out/test09_manyiters/01/out/test_T_iter{0:03d}.npy".format(i)))

    
X[-1,:] = np.ravel(np.load("../out/test02_md_method/01_arith/out/test_T_ref.npy"))

clf = sm.MDS(n_components=2)
X_mds = clf.fit_transform((X))
#X_mds = clf.fit_transform(np.log10(X))
print("Done. Stress: %f" % clf.stress_)

#print(X_mds)

pl.scatter(X_mds[:-1,0], X_mds[:-1,1])
pl.scatter(X_mds[-1,1], X_mds[-1,1], color="red")




# for i, label in enumerate(labels):
#     pl.scatter(X_mds[i,0], X_mds[i,1], label=label)
#pl.legend()    
pl.show()






