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



diagn.append({"file": "../out/test10_md_natural/01_00/out/diagn.csv", "nbd": "0°" })
diagn.append({"file": "../out/test10_md_natural/02_00-10/out/diagn.csv",  "nbd": "0°, 10°"})
diagn.append({"file": "../out/test10_md_natural/03_00-10-20/out/diagn.csv",  "nbd": "0°, 10°, 20°"})
diagn.append({"file": "../out/test10_md_natural/04_00-10-20-30/out/diagn.csv",  "nbd": "0°, 10°, 20°, 30°"})




for dia in diagn:
    data = pd.read_csv(dia["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    pl.plot(it, data["lmbd2"], "-o", label="{0}".format(dia["nbd"]))

pl.xlabel("iteration")
pl.title("$\lambda^2$")    
pl.legend()
pl.savefig("nbd_diagn.png", dpi=400)
pl.savefig("nbd_diagn.pdf")
pl.show()    
    

