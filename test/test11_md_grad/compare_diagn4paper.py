#!/usr/bin/env python3
"""
:This file:

    `compare_diagn4paper.py`

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
import pandas as pd
import matplotlib.pylab as pl

diagn1 = []
diagn2 = []



diagn1.append({"file": "../out/test11_md_grad/01_00-10-20-30_gr0d001_std00/out/diagn.csv", "nbd": "0.001, 0" })
diagn1.append({"file": "../out/test11_md_grad/02_00-10-20-30_gr0d001_std05/out/diagn.csv",  "nbd": "0.001, 5"})
diagn1.append({"file": "../out/test11_md_grad/03_00-10-20-30_gr0d001_std10/out/diagn.csv",  "nbd": "0.001, 10"})
diagn1.append({"file": "../out/test11_md_grad/04_00-10-20-30_gr0d001_std20/out/diagn.csv",  "nbd": "0.001, 20"})

diagn2.append({"file": "../out/test11_md_grad/05_00-10-20-30_gr0d002_std00/out/diagn.csv",  "nbd": "0 cm"})
diagn2.append({"file": "../out/test11_md_grad/06_00-10-20-30_gr0d002_std05/out/diagn.csv",  "nbd": "5 cm"})
diagn2.append({"file": "../out/test11_md_grad/07_00-10-20-30_gr0d002_std10/out/diagn.csv",  "nbd": "10 cm"})
diagn2.append({"file": "../out/test11_md_grad/08_00-10-20-30_gr0d002_std20/out/diagn.csv",  "nbd": "20 cm"})

# diagn2.append({"file": "../out/test11_md_grad/05_00-10-20-30_gr0d002_std00/out/diagn.csv",  "nbd": "0.002 0"})
# diagn2.append({"file": "../out/test11_md_grad/06_00-10-20-30_gr0d002_std05/out/diagn.csv",  "nbd": "0.002 05"})
# diagn2.append({"file": "../out/test11_md_grad/07_00-10-20-30_gr0d002_std10/out/diagn.csv",  "nbd": "0.002 10"})
# diagn2.append({"file": "../out/test11_md_grad/08_00-10-20-30_gr0d002_std20/out/diagn.csv",  "nbd": "0.002 20"})




for dia in diagn1:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-x") 
#    pl.plot(it, data["lmbd2"], "-v", label="{0}".format(dia["nbd"]))   

pl.gca().set_prop_cycle(None)

for dia in diagn2:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-+")

pl.gca().set_prop_cycle(None)

# THis is useless, only for defining a different style in the legend
for dia in diagn2:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], label="{0}".format(dia["nbd"]))
    
pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("nbd_diagn4paper.png", dpi=400)
pl.savefig("nbd_diagn4paper.pdf")
pl.show()    
    

