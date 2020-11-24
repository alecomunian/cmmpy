* In the documentation it is suggested to modify the `matplotlibrc`
  configuration file in order to add in the LaTeX preamble the package
  ``siunitx``.  In some cases this might not work. An alternative is
  to define explicitly in the `tools.py` file with the line::
 
      pl.rc('text.latex', preamble=r'\usepackage{siunitx}')

* In some situation, when running a script and saving a figure with
  LaTeX might create some problems, for example by claiming that some
  `sty` file is missing (for example, file `type1ec.sty`). For the
  file `type1ec.sty`, one possible solution is to install, from the
  package manager, the package `cm-super`, containing some required
  fonts.

  


  
