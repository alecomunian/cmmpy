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

    `run_cmm.py`

:Purpose:

    Run the CMM.

:Usage:

    From the command line::

      ./run_cmm.py <file.json>

    For example, you could use::

      ./run_cmm.py template/test.json

:Parameters:

    <file.json>
        This is a JSON file containing all the parameters required to run the CMM.
        See the file `template/test.json` for more details.

:Version:

    0.1 , YYYY-MM-DD :

:Authors:

    Alessandro Comunian

"""
import os
import sys
import json
import numpy as np
import scipy.stats as ss
import pandas as pd
import copy
import logging
import timeit

import cmmpy.tools as tools
import cmmpy.cmm as cmm

start = timeit.default_timer()

# Get the name of the parameters file
try:
    file_json = sys.argv[1]
except IndexError:
    sys.exit("    ERROR: no parameter (JSON) input file provided!")

# Read an external file containing the parameters
with open(file_json, "r") as json_in:
    par = json.load(json_in)

#    
# Initialize some parameters
#
nb_iter = par["cmm"]["nb_iter"]
# Get the number of data sets
nb_ds = len(par["fwd"]["data_sets"])
    
# Read and move to the working directory    
wdir = par["general"]["wdir"]
out_dir = par["general"]["out"]

# Move to the working directory
if not os.path.exists(wdir):
    os.makedirs(wdir)
os.chdir(wdir)
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
    
# Set up logging to file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S',
                    filename='{0}.log'.format(par["fwd"]["name"]),
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)-16s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.info("===========================")
logging.info("=== Starting CMM script ===")
logging.info("===========================")
logging.info('Working directory: "{0}"'.format(wdir))
logging.info('Number of CMM interations: {0}'.format(nb_iter))
logging.info('Number of data sets: {0}'.format(nb_ds))

# Create a reference heterogeneity
logging.info("Creating reference T.")
t_ref = tools.create_t_ref(par)
t_minmax = (np.min(t_ref), np.max(t_ref))
k_ref = t_ref # thickness =1

# Plot ref T
tools.plot_t2(t_ref, par["fwd"]["name"], out_dir=out_dir,
             mode="ref")
np.save(os.path.join("out", "{0}_T_ref.npy".format(par["fwd"]["name"])), t_ref)

# =============================================================================
# Define here the boundary conditions
# =============================================================================

# Read an external file containing the shape of the domain
bcs = np.fliplr(np.transpose(np.loadtxt(os.path.join(par["general"]["data"],
                                                     par["fwd"]["bcs"]),
                                        dtype="U1")))
domain = np.zeros(bcs.shape)
domain[bcs=="E"] = 1 # External cells
domain[bcs=="D"] = 2 # Dirichlet BCs
domain[bcs=="I"] = 3 # Internal cells

tools.plot_domain(domain, out_dir, par)

# Read h (to be used as fixed head BCs) from an external file
spd_h = [None]*nb_ds
h_ref = [None]*nb_ds 
gcol_ref = [None]*nb_ds
grow_ref = [None]*nb_ds
gmod_ref = [None]*nb_ds
spdis = [None]*nb_ds
par["cmm"]["c"] = [None]*nb_ds

for i in range(nb_ds):
    # Read the fixed head BCs
    spd_h[i] = tools.vtk2Dto_spd_h(par, i)

    # Set the directory that will contain all the output
    cout_dir = os.path.join(out_dir, "ref", "ds{0:03d}".format(i))

    # Solve the FP
    logging.info("*** Preliminar FP run to define the refence h ***")
    h_ref[i], gcol_ref[i], grow_ref[i], gmod_ref[i], spdis[i] = tools.run_fp(
        par, spd_h[i], k_ref, sdir="ref", ds=i, noise=True)

#    tools.plot_h(h_ref[i], "ref/ds{0:03d}".format(i), mode="ref")
#    print(os.getcwd())
    tools.save_h_vtk(h_ref[i], par, "out/ref/ds{0:03d}".format(i))
    tools.plot_domain(domain, cout_dir, par, i)
    
    beta_size, par["cmm"]["c"][i] = cmm.beta_size2(gmod_ref[i], par["cmm"])
    logging.info("Corrected gradients (Beta) : {0:3.2f} % (c={1:.2e})".format( beta_size, par["cmm"]["c"][i]))

# Initial value for T
# (for simplicity, we can start with the geometric mean of t_ref
t_cm = ss.gmean(t_ref, axis=None)*np.ones(t_ref.shape)

# Allocate some containers useful to store errors...
lmbd = np.zeros((nb_iter))
lmbd_abs = np.zeros((nb_iter))
lmbd2 = np.zeros((nb_iter))

t_cmds = np.zeros([nb_ds]+list(t_cm.shape))
h_cmds = [None]*nb_ds
gcol_cmds = [None]*nb_ds
grow_cmds = [None]*nb_ds
gmod_cmds = [None]*nb_ds
spdis_cmds = [None]*nb_ds
flow_cmds = [None]*nb_ds
A = np.zeros(h_ref[0].shape)
anomaly = np.zeros((nb_iter, nb_ds))
# Intial value for h
for i in range(nb_iter):
    logging.info("*** START: CMM iteration {0:3d}/{1} ***".format(i+1, nb_iter))
    # This is the main directory where the FP will run
    sdir = "iter{0:03d}".format(i)

    # Plot the T field used in this step
    # WARNING: This plot corresponds to the results of the previous iteration
    # (or to the initial value for i=0)
    tools.plot_t2(t_cm, par["fwd"]["name"], out_dir=out_dir,
                  mode="iter", it=i, minmax=t_minmax)

    # Solve a FP for the current t_cm
    k_cm = copy.copy(t_cm)  # (thickess = 1)

    for j in range(nb_ds):
        sdir_ds = os.path.join(sdir, "ds{0:03}".format(j))
        logging.info('Running FP, workspace "{0}"...'.format(sdir_ds))     
        h_cmds[j], gcol_cmds[j], grow_cmds[j], gmod_cmds[j], spdis_cmds[j] = tools.run_fp(
            par, spd_h[j], k_cm, sdir=sdir, ds=j)
        flow_cmds[j] = tools.spdis2mat(spdis_cmds[j], par["fwd"]["ny"], par["fwd"]["nx"])

        # Compute head anomaly
        A = h_cmds[j] - h_ref[j]

        tools.plot_A(A, sdir_ds, i)
        np.save(os.path.join("out", sdir_ds, "A.npy"), A)

        anomaly[i,j] = np.mean(np.abs(A))
        
        t_cmds[j,:,:,:] = cmm.update_t2(h_cmds[j], gmod_cmds[j], h_ref[j], gmod_ref[j], t_cm, t_minmax, par["cmm"], j)

    t_cm = tools.merge_t(t_cmds, t_cm, mode=par["cmm"]["mode"], grad=[gcol_cmds, grow_cmds], flow=flow_cmds)
    # This should be the computed T corresponding to the right simulation step    
    np.save(os.path.join("out", "{0}_T_iter{1:03d}.npy".format(par["fwd"]["name"],i)), t_cm)

    # Plot the error on T
    tools.plot_t_err2(t_ref, t_cm, par["fwd"]["name"], out_dir, i)

    # Compute some errors
    lmbd[i] = np.sum(np.log10(t_cm) - np.log10(t_ref))/t_ref.size
    lmbd_abs[i] = np.sum(np.abs(np.log10(t_cm) - np.log10(t_ref)))/t_ref.size
    lmbd2[i] = np.sum((np.log10(t_cm) - np.log10(t_ref))**2)/t_ref.size
    
    
    logging.info("*** STOP:  CMM iteration {0:3d}/{1} ***".format(i+1, nb_iter))

    
ddict = {"lmbd": lmbd, "lmbd_abs": lmbd_abs, "lmbd2": lmbd2}

for j in range(nb_ds):
    ddict["a{0}".format(j)] = anomaly[:,j]
    
diagn = pd.DataFrame(ddict)

diagn.to_csv(os.path.join(out_dir, "diagn.csv"), float_format="%.4e",
             index=False)
tools.plot_diagn(diagn)

stop = timeit.default_timer()

logging.info("===========================")
logging.info("=== Stopping CMM script ===")
logging.info("===========================")
logging.info("Execution time: {0:10.2f} [sec]".format(stop-start))

