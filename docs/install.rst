Installation
================================

Installing and using `cmmpy` should be relatively easy, and thanks to
Python's flexibility, that should be feasible on many operative
systems (OSs), including MS Windows, Mac OS X and Linux.

|
Requirements
-----------------------

To use the `cmmpy` module you need a standard Python3.X installation,
together with the main mathematical and plotting libraries (``numpy``,
``pandas``, ``matplotlib`` etc), and the USGS package ``flopy``.  If
``pip`` is used for the installation, all there requirement should be
automatically.

Clearly, if you have installed ``flopy`` then you should also have
installed the binaries related to the corresponding MODFLOW package.

.. note:: The current version of ``cmmpy`` is based on MODFLOW6
          compiled with the `double` option.
|
Installation
-------------------------------

The suggested way is to use ``pip`` (which should be also already
available with `Anaconda`).

``cmmpy`` is available at the `Python Package Index repository
<https://pypi.org/project/cmmpy/>`_. Therefore, in can be easily
installed (together with its dependencies) with the command::

    pip install cmmpy

Alternatively, if you prefer to download the sources from
`https://bitbucket.org/alecomunian/cmmpy
<https://bitbucket.org/alecomunian/cmmpy>`_, you can:

1) Clone or download this repository on your hard drive.
2) If required, unpack it and ``cd cmmpy``.
3) Inside the project directory, from the command line::

     pip install -e .

4) To check if it worked, open a Python terminal and try::

     import cmmpy
