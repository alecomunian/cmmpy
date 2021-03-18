Tutorial
==============

This is a brief tutorial to illustrate how to run a simple application
that makes use of the CMM. For more details and more options, one can
have a look at many examples avaiable in the bitbucket/github
reposotories in the folder `test`. The files provided in the test
folder cover almost all the examples explored in the companion paper
published in Computers and Geosciences by A.Comunian and M.Giudici,
DOI: `10.1016/j.cageo.2021.104705
<https://doi.org/10.1016/j.cageo.2021.104705>`_ (hereinafter, the
*companion paper*).

Example 1 - Tomographic approach
*******************************************

This example is based on the implementation of the CMM with a
tomographic approach. It should allow to obtain part e) of Fig.9 of
the companion paper.

Hereinafter we will briefly describe the main components required to
run the CMM.

Setting up the forward problem
-------------------------------------

As many other inversion tools, the CMM requires to set up a tool to
solve the forward problem (FP). Here the set up is implemented with
``flopy`` and the ``Modflow6`` version. Nevertheless, you can
customize the code to use different tools for the solution of the FP,
as it was for example done in the preliminary part of this study by
using ``Modflow2005``, or by Comunian and Giudici (DOI:
`10.1007/s11004-018-9727-0
<https://doi.org/10.1007/s11004-018-9727-0>`_) who applied the CMM
with `Parflow <https://www.parflow.org/>`_ as flow simulation engine.

In the provided Python code, this is done in the function ``run_fp``
of the module ``tool``. You can customize this function to suit your
particular needs. However, if your have modelling assuption akin to
the one stated in the companion paper, then you will not need to
customize this function too much, maybe even not. In fact, the code is
written delegate as much as possbile all the parameterization and a
big part of the model settings to an editable ``json`` file, in order
to avoid as much as possible edits on the function ``run_fp``
function. The content of this ``json`` file is described in the next
section.


Parameter file
--------------------

As mentioned in the previous section, the main modifications that a
user should do to apply the CMM to his case study should be made on
the data files and to the input parameter file (JSON file). An example
of this file is provided for many test cases in the bitbucket/github
repositories in the aforementioned `test` folder. For example,
hereinafter it is provided a list of the entries of the file ``test.json`` contained in the
folder ``test/test07_md_paper``, explained one by one.
In general, the parameters are grouped into four categories:

``general``
    Contains some "general" parameters.
    ``sdfg``
        ciccio
    ``pollo``
        serg
``fwd``
    All the parameters related to the forward problem run.
``t_gen``
    All the parameters related to the generation of the syntetic :math:`T` distribution
    which is used as reference.
``cmm``
    Here the parameters related to the Comparison Model Method (CMM).
``noise``
    Here the parameters related to the addition of noise to the input head fields.
    

``general->wdir``
    This is the working directory that will contain all the output of the CMM run.
general-data
    Directory containing the input data, like for example the files with the boundary
    conditions and the shape of the domain (see for example the folder into ``test/data``).
general-out
    Output folder
fwd-ws
    The workspace related to the Modflow problem
fwd-name
    Name of the modflow problem
exe_name
    The name of the modflow executable. In the example, the name ``mf6dbl`` is provided. However, in general,
    a more common name would be ``mf6`` (if you are working on Linux of macOS) or ``mf6.exe``.
    Clearly, if the binary file of your modflow is not in the system PATH, you could also set
    here the explicit path.
bcs
    A file that contains codes that indicate  the type of the cells used for the boundary conditions.
    See the next section for more details.
nx, ny
    Numer of cells along the :math:`x` and :math:`y` coordinates
dx, dy
    Size of the cells side (in meters)
name


Input data files
---------------------------
bla bla.


    



