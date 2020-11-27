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
    data = pd.read_csv(diagn["file"])
    it = np.arange(1, data["lmbd2"].size+1)
    ax.plot(it, data["lmbd2"], "-", label="{0}".format(diagn["std"]))
    if not diagn["lh"]:
        ax.text(it[-1]+0.2, data["lmbd2"].iloc[-1], "{0:4.2f}".format(diagn["std"]), va="center")
#    ax.legend()
    
diagn = {}

# South direction
diagn["01S"] = {"file": "../out/test08_noise/01_std00_S/out/diagn.csv", "std": 0.00, "data": "S", 'lh': False }
diagn["02S"] = {"file": "../out/test08_noise/01_std01_S/out/diagn.csv", "std": 0.01, "data": "S", 'lh': True }
diagn["03S"] = {"file": "../out/test08_noise/01_std02_S/out/diagn.csv", "std": 0.02, "data": "S", 'lh': True }
diagn["04S"] = {"file": "../out/test08_noise/01_std03_S/out/diagn.csv", "std": 0.03, "data": "S", 'lh': False }
diagn["05S"] = {"file": "../out/test08_noise/01_std04_S/out/diagn.csv", "std": 0.04, "data": "S", 'lh': False }
diagn["06S"] = {"file": "../out/test08_noise/01_std05_S/out/diagn.csv", "std": 0.05, "data": "S", 'lh': False }
diagn["07S"] = {"file": "../out/test08_noise/01_std06_S/out/diagn.csv", "std": 0.06, "data": "S", 'lh': False }
diagn["08S"] = {"file": "../out/test08_noise/01_std07_S/out/diagn.csv", "std": 0.07, "data": "S", 'lh': False }
diagn["09S"] = {"file": "../out/test08_noise/01_std08_S/out/diagn.csv", "std": 0.08, "data": "S", 'lh': False }
diagn["10S"] = {"file": "../out/test08_noise/01_std09_S/out/diagn.csv", "std": 0.09, "data": "S", 'lh': False }
diagn["11S"] = {"file": "../out/test08_noise/01_std10_S/out/diagn.csv", "std": 0.10, "data": "S", 'lh': False }

# S+SW
diagn["01S-SW"] = {"file": "../out/test08_noise/02_std00_S-SW/out/diagn.csv", "std": 0.00, "data": "S-SW", 'lh': False }
diagn["02S-SW"] = {"file": "../out/test08_noise/02_std01_S-SW/out/diagn.csv", "std": 0.01, "data": "S-SW", 'lh': True }
diagn["03S-SW"] = {"file": "../out/test08_noise/02_std02_S-SW/out/diagn.csv", "std": 0.02, "data": "S-SW", 'lh': True }
diagn["04S-SW"] = {"file": "../out/test08_noise/02_std03_S-SW/out/diagn.csv", "std": 0.03, "data": "S-SW", 'lh': True }
diagn["05S-SW"] = {"file": "../out/test08_noise/02_std04_S-SW/out/diagn.csv", "std": 0.04, "data": "S-SW", 'lh': False }
diagn["06S-SW"] = {"file": "../out/test08_noise/02_std05_S-SW/out/diagn.csv", "std": 0.05, "data": "S-SW", 'lh': True }
diagn["07S-SW"] = {"file": "../out/test08_noise/02_std06_S-SW/out/diagn.csv", "std": 0.06, "data": "S-SW", 'lh': False }
diagn["08S-SW"] = {"file": "../out/test08_noise/02_std07_S-SW/out/diagn.csv", "std": 0.07, "data": "S-SW", 'lh': False }
diagn["09S-SW"] = {"file": "../out/test08_noise/02_std08_S-SW/out/diagn.csv", "std": 0.08, "data": "S-SW", 'lh': False }
diagn["10S-SW"] = {"file": "../out/test08_noise/02_std09_S-SW/out/diagn.csv", "std": 0.09, "data": "S-SW", 'lh': False }
diagn["11S-SW"] = {"file": "../out/test08_noise/02_std10_S-SW/out/diagn.csv", "std": 0.10, "data": "S-SW", 'lh': False }

# S+SW+W+NW
diagn["01S-SW-W-NW"] = {"file": "../out/test08_noise/04_std00_S-SW-W-NW/out/diagn.csv", "std": 0.00, "data": "S-SW-W-NW", 'lh': False }
diagn["02S-SW-W-NW"] = {"file": "../out/test08_noise/04_std01_S-SW-W-NW/out/diagn.csv", "std": 0.01, "data": "S-SW-W-NW", 'lh': True }
diagn["03S-SW-W-NW"] = {"file": "../out/test08_noise/04_std02_S-SW-W-NW/out/diagn.csv", "std": 0.02, "data": "S-SW-W-NW", 'lh': True }
diagn["04S-SW-W-NW"] = {"file": "../out/test08_noise/04_std03_S-SW-W-NW/out/diagn.csv", "std": 0.03, "data": "S-SW-W-NW", 'lh': True }
diagn["05S-SW-W-NW"] = {"file": "../out/test08_noise/04_std04_S-SW-W-NW/out/diagn.csv", "std": 0.04, "data": "S-SW-W-NW", 'lh': True }
diagn["06S-SW-W-NW"] = {"file": "../out/test08_noise/04_std05_S-SW-W-NW/out/diagn.csv", "std": 0.05, "data": "S-SW-W-NW", 'lh': False }
diagn["07S-SW-W-NW"] = {"file": "../out/test08_noise/04_std06_S-SW-W-NW/out/diagn.csv", "std": 0.06, "data": "S-SW-W-NW", 'lh': True }
diagn["08S-SW-W-NW"] = {"file": "../out/test08_noise/04_std07_S-SW-W-NW/out/diagn.csv", "std": 0.07, "data": "S-SW-W-NW", 'lh': False }
diagn["09S-SW-W-NW"] = {"file": "../out/test08_noise/04_std08_S-SW-W-NW/out/diagn.csv", "std": 0.08, "data": "S-SW-W-NW", 'lh': False }
diagn["10S-SW-W-NW"] = {"file": "../out/test08_noise/04_std09_S-SW-W-NW/out/diagn.csv", "std": 0.09, "data": "S-SW-W-NW", 'lh': False }
diagn["11S-SW-W-NW"] = {"file": "../out/test08_noise/04_std10_S-SW-W-NW/out/diagn.csv", "std": 0.10, "data": "S-SW-W-NW", 'lh': False }




    

fig, ax = pl.subplots(1,3, sharex=True, sharey=True, figsize=(12,4))

ax[0].set_title("a) $\lambda^2$ - data sets S, W, SW and NW")
plotta(diagn["01S-SW-W-NW"], ax[0])
plotta(diagn["02S-SW-W-NW"], ax[0])
plotta(diagn["03S-SW-W-NW"], ax[0])
plotta(diagn["04S-SW-W-NW"], ax[0])
plotta(diagn["05S-SW-W-NW"], ax[0])
plotta(diagn["06S-SW-W-NW"], ax[0])
plotta(diagn["07S-SW-W-NW"], ax[0])
plotta(diagn["08S-SW-W-NW"], ax[0])
plotta(diagn["09S-SW-W-NW"], ax[0])
plotta(diagn["10S-SW-W-NW"], ax[0])
plotta(diagn["11S-SW-W-NW"], ax[0])
ax[0].set_xlim((0, 12))
ax[0].set_xlabel("CMM iteration")
#ax[0].grid()

ax[1].set_title("b) $\lambda^2$ - data sets S and W")
plotta(diagn["01S-SW"], ax[1])
plotta(diagn["02S-SW"], ax[1])
plotta(diagn["03S-SW"], ax[1])
plotta(diagn["04S-SW"], ax[1])
plotta(diagn["05S-SW"], ax[1])
plotta(diagn["06S-SW"], ax[1])
plotta(diagn["07S-SW"], ax[1])
plotta(diagn["08S-SW"], ax[1])
plotta(diagn["09S-SW"], ax[1])
plotta(diagn["10S-SW"], ax[1])
plotta(diagn["11S-SW"], ax[1])
ax[1].set_xlabel("CMM iteration")

ax[2].set_title("c)  $\lambda^2$ - data set S")
plotta(diagn["01S"], ax[2])
plotta(diagn["02S"], ax[2])
plotta(diagn["03S"], ax[2])
plotta(diagn["04S"], ax[2])
plotta(diagn["05S"], ax[2])
plotta(diagn["06S"], ax[2])
plotta(diagn["07S"], ax[2])
plotta(diagn["08S"], ax[2])
plotta(diagn["09S"], ax[2])
plotta(diagn["10S"], ax[2])
plotta(diagn["11S"], ax[2])

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
    

