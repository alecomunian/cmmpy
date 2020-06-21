#!/usr/bin/env python3
"""
:License:
    This file is part of cmmpy.

    cmmpy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    cmmpy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with cmmpy.  If not, see <https://www.gnu.org/licenses/>.

:This file:

    `run_all.py`

:Purpose:

    Run a many CMM simulations.

:Usage:

    You can run it from the command line by using something like::

      ./run_all.py <directory>

    Where in the place of  <directory> you should put a directory containing
    a number of sub-directories containing a JSON file containing the 
    required run parameters. 

:Parameters:

:Version:

    0.1 , YYYY-MM-DD :


:Authors:

    Alessandro Comunian

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
    print(run_string)
    os.system(run_string)

