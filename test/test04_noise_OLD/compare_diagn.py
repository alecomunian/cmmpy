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
import pandas as pd
import matplotlib.pylab as pl

diagn = []



diagn.append({"file": "01_std000/out/diagn.csv", "std": 0.0 })
diagn.append({"file": "02_std001/out/diagn.csv", "std": 0.01 })
diagn.append({"file": "03_std010/out/diagn.csv", "std": 0.1 })
#diagn.append({"file": "04_std100/out/diagn.csv", "std": 1.0 })
diagn.append({"file": "05_std020/out/diagn.csv", "std": 0.2 })
diagn.append({"file": "06_std030/out/diagn.csv", "std": 0.3 })
diagn.append({"file": "07_std050/out/diagn.csv", "std": 0.5 })





for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}".format(dia["std"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("noise_diagn.png", dpi=400)
pl.show()    
    

