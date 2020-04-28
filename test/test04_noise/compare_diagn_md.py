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

def plotta(diagn, ax):
    data = pd.read_csv(diagn["dir"])
    it = np.arange(1, data["lmbd2"].size+1)
    ax.plot(it, data["lmbd2"], "-", label="{0}".format(diagn["std"]))
    if not diagn["lh"]:
        ax.text(it[-1]+0.2, data["lmbd2"].iloc[-1], "{0:4.2f}".format(diagn["std"]), va="center")
#    ax.legend()
    
diagn = {}
diagn["08"] = {"dir": "08_std001_N-E-NE-SE/out/diagn.csv", "std": 0.01, "data": "N-E-NE-SE", "lh": False}
diagn["09"] = {"dir": "09_std002_N-E-NE-SE/out/diagn.csv", "std": 0.02, "data": "N-E-NE-SE", "lh": True}
diagn["10"] = {"dir": "10_std003_N-E-NE-SE/out/diagn.csv", "std": 0.03, "data": "N-E-NE-SE", "lh": True}
diagn["11"] = {"dir": "11_std004_N-E-NE-SE/out/diagn.csv", "std": 0.04, "data": "N-E-NE-SE", "lh": True}
diagn["12"] = {"dir": "12_std005_N-E-NE-SE/out/diagn.csv", "std": 0.05, "data": "N-E-NE-SE", "lh": False}
diagn["13"] = {"dir": "13_std006_N-E-NE-SE/out/diagn.csv", "std": 0.06, "data": "N-E-NE-SE", "lh": True}
diagn["14"] = {"dir": "14_std007_N-E-NE-SE/out/diagn.csv", "std": 0.07, "data": "N-E-NE-SE", "lh": False}
diagn["15"] = {"dir": "15_std008_N-E-NE-SE/out/diagn.csv", "std": 0.08, "data": "N-E-NE-SE", "lh": True}
diagn["16"] = {"dir": "16_std009_N-E-NE-SE/out/diagn.csv", "std": 0.09, "data": "N-E-NE-SE", "lh": False}
diagn["17"] = {"dir": "17_std010_N-E-NE-SE/out/diagn.csv", "std": 0.10, "data": "N-E-NE-SE", "lh": False}
diagn["18"] = {"dir": "18_std011_N-E-NE-SE/out/diagn.csv", "std": 0.11, "data": "N-E-NE-SE", "lh": False}


diagn["19"] = {"dir": "19_std001_N-E/out/diagn.csv", "std": 0.01, "data": "N-E", "lh": False}
diagn["20"] = {"dir": "20_std002_N-E/out/diagn.csv", "std": 0.02, "data": "N-E", "lh": True}
diagn["21"] = {"dir": "21_std003_N-E/out/diagn.csv", "std": 0.03, "data": "N-E", "lh": True}
diagn["22"] = {"dir": "22_std004_N-E/out/diagn.csv", "std": 0.04, "data": "N-E", "lh": False}
diagn["23"] = {"dir": "23_std005_N-E/out/diagn.csv", "std": 0.05, "data": "N-E", "lh": False}
diagn["24"] = {"dir": "24_std006_N-E/out/diagn.csv", "std": 0.06, "data": "N-E", "lh": False}
diagn["25"] = {"dir": "25_std007_N-E/out/diagn.csv", "std": 0.07, "data": "N-E", "lh": False}
diagn["26"] = {"dir": "26_std008_N-E/out/diagn.csv", "std": 0.08, "data": "N-E", "lh": False}
diagn["27"] = {"dir": "27_std009_N-E/out/diagn.csv", "std": 0.09, "data": "N-E", "lh": False}
diagn["28"] = {"dir": "28_std010_N-E/out/diagn.csv", "std": 0.10, "data": "N-E", "lh": False}


diagn["29"] = {"dir": "29_std001_N/out/diagn.csv", "std": 0.01, "data": "N", "lh": False}
diagn["30"] = {"dir": "30_std002_N/out/diagn.csv", "std": 0.02, "data": "N", "lh": False}
diagn["31"] = {"dir": "31_std003_N/out/diagn.csv", "std": 0.03, "data": "N", "lh": False}
diagn["32"] = {"dir": "32_std004_N/out/diagn.csv", "std": 0.04, "data": "N", "lh": False}
diagn["33"] = {"dir": "33_std005_N/out/diagn.csv", "std": 0.05, "data": "N", "lh": False}
diagn["34"] = {"dir": "34_std006_N/out/diagn.csv", "std": 0.06, "data": "N", "lh": False}
diagn["35"] = {"dir": "35_std007_N/out/diagn.csv", "std": 0.07, "data": "N", "lh": False}
diagn["36"] = {"dir": "36_std008_N/out/diagn.csv", "std": 0.08, "data": "N", "lh": False}
diagn["37"] = {"dir": "37_std009_N/out/diagn.csv", "std": 0.09, "data": "N", "lh": False}
diagn["38"] = {"dir": "38_std010_N/out/diagn.csv", "std": 0.10, "data": "N", "lh": False}


    

fig, ax = pl.subplots(1,3, sharex=True, sharey=True, figsize=(12,4))

ax[0].set_title("a) $\lambda^2$ - data sets S, W, SW and NW")
plotta(diagn["08"], ax[0])
plotta(diagn["09"], ax[0])
plotta(diagn["10"], ax[0])
plotta(diagn["11"], ax[0])
plotta(diagn["12"], ax[0])
plotta(diagn["13"], ax[0])
plotta(diagn["14"], ax[0])
plotta(diagn["15"], ax[0])
plotta(diagn["16"], ax[0])
plotta(diagn["17"], ax[0])
ax[0].set_xlim((0, 12))
ax[0].set_xlabel("CMM iteration")
#ax[0].grid()

ax[1].set_title("b) $\lambda^2$ - data sets S and W")
plotta(diagn["19"], ax[1])
plotta(diagn["20"], ax[1])
plotta(diagn["21"], ax[1])
plotta(diagn["22"], ax[1])
plotta(diagn["23"], ax[1])
plotta(diagn["24"], ax[1])
plotta(diagn["25"], ax[1])
plotta(diagn["26"], ax[1])
plotta(diagn["27"], ax[1])
plotta(diagn["28"], ax[1])
ax[1].set_xlabel("CMM iteration")

ax[2].set_title("c)  $\lambda^2$ - data set S")
plotta(diagn["29"], ax[2])
plotta(diagn["30"], ax[2])
plotta(diagn["31"], ax[2])
plotta(diagn["32"], ax[2])
plotta(diagn["33"], ax[2])
plotta(diagn["34"], ax[2])
plotta(diagn["35"], ax[2])
plotta(diagn["36"], ax[2])
plotta(diagn["37"], ax[2])
plotta(diagn["38"], ax[2])
ax[2].set_xlabel("CMM iteration")

#plotta(diagn["18"], ax[0,0])

# plotta("E-N", diagn, ax[0,0])
# plotta("E-N-NE", diagn, ax[0,0])
# plotta("E-N-NE-SE", diagn, ax[0,0])



# ax[0,0].set_title("a)")


# plotta("E", diagn, ax[0,1])
# plotta("E-N", diagn, ax[0,1])
# plotta("E-N-SE", diagn, ax[0,1])
# plotta("E-N-SE-NE", diagn, ax[0,1])



# ax[0,1].set_title("b)")

# plotta("NE", diagn, ax[1,0])
# plotta("NE-SE", diagn, ax[1,0])
# plotta("NE-SE-E", diagn, ax[1,0])
# plotta("NE-SE-E-N", diagn, ax[1,0])



# ax[1,0].set_title("c)")

# plotta("E", diagn, ax[1,1])
# plotta("E-NE", diagn, ax[1,1])
# plotta("E-NE-N", diagn, ax[1,1])
# plotta("E-NE-N-SE", diagn, ax[1,1])



# ax[1,1].set_title("d)")







# ax[1,0].set_xlabel("iteration")
# ax[1,1].set_xlabel("iteration")
# ax[1,0].set_ylabel("$\lambda^2$")
# ax[0,0].set_ylabel("$\lambda^2$")    
pl.tight_layout()

pl.savefig("std-nbdata_diagn.png", dpi=400)
pl.savefig("std-nbdata_diagn.pdf")
pl.show()    
    

