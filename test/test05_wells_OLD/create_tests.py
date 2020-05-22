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
import sys
import os
import json

file_json = sys.argv[1]


# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)

wdirs = ["pollettoA", "pollettoB"]
nb_iter = [2, 3]
wells_nb = [3,4]
ds_nb = [1,2]

# Set here the working directory

cwd = os.path.basename(os.getcwd())
par["general"]["data"] = "../../../data"

for i, wdir in enumerate(wdirs):
    # Create the working directory
    if not os.path.exists(wdir):
        os.makedirs(wdir)

    par["general"]["wdir"] = os.path.join(cwd, wdir)
    par["cmm"]["nb_iter"] = nb_iter[i]
    for j in ds_nb[i]:
        par["fwd"]["data_sets"]["ds{0:03d}".format(j)]["h_BCs"] = par["fwd"]["data_sets"]["template"]["h_BCs"]
        par["fwd"]["data_sets"]["ds{0:03d}".format(j)]["rch"] = par["fwd"]["data_sets"]["template"]["rch"]
        par["fwd"]["data_sets"]["ds{0:03d}".format(j)]["wells_loc"] = par["fwd"]["data_sets"]["template"]["wells_loc"]        

    # Save the JSON into the working directory
    file_out = os.path.join(wdir, "test.json")

    with open(file_out, 'w', encoding='utf-8') as f:
        json.dump(par, f, ensure_ascii=False, indent=4)
