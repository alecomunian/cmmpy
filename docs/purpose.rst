Purpose
=====================

This is a python implementation of the Comparison Model Method (CMM),
a direct method to solve inverse problems in hydrogeology, and in
particular to compute the hydraulic conductivity *T* of a confined
aquifer given an initial tentative value of *T* and one or more
interpolated hydraulic head fields *h*.  This implementation of the
CMM heavily relies on the USGS engines of the `Modflow
<https://www.usgs.gov/mission-areas/water-resources/science/modflow-and-related-programs>`_
family (and `Modflow6
<https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model>`_
in particular) to solve the forward problem, facilitated by the use of
the Python module `flopy
<https://www.usgs.gov/software/flopy-python-package-creating-running-and-post-processing-modflow-based-models>`_. Nevertheless,
it can be adapted to make use of other engines for the solution of the
forward problem.

|
