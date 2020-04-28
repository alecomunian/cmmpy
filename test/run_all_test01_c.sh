#!/bin/bash
#
# :This File:
#
#     `bash_simple.sh`
#
# :Purpose:
#
#     A sample bash script
#
# :Usage:
#
#     Explain here the usage.
#
# :Parameters:
#
#     Here the input parameters
#
# :Version:
#
#     0.1 , YYYY-MM-DD :
#
#         * First version
#
# :Authors:
#
#     Alessandro Comunian
#
# .. notes::
#
# .. warnings::
#
# .. limitations::
#

#workon dirinv


./run_cmm.py ./test01_c/01_perc100/test.json > 01.tmp &
./run_cmm.py ./test01_c/02_perc060/test.json > 02.tmp &
./run_cmm.py ./test01_c/03_perc030/test.json > 03.tmp &
./run_cmm.py ./test01_c/04_perc015/test.json > 04.tmp &
./run_cmm.py ./test01_c/05_perc000/test.json > 05.tmp &



