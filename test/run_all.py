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
import os
import sys
import glob
import subprocess

root_dir = sys.argv[1]

print('    Performing all simulations in the directory "{0}"'.format(root_dir))

dirs = glob.glob("./{0}/**/".format(root_dir))

for i, dir in enumerate(dirs):
    run_string = "./run_cmm.py "+dir+"test.json"+" > "+"./tmp/{0}_{1:02d}.tmp &".format(root_dir, i+1)
    os.system(run_string)

