Hereinafter the description of the content of the test cases provided
with the `cmmpy` package.

Preliminary remark: all the `test` folders but `test13_real` contain
the complete workflow used to perform the tests contained in the
*companion paper* (Comunian and Giudici, Computers and Geosciences,
2021). Therefore, the information provided and the script `run_cmm.py`
allows to:
1) Create a syntetic *T* field.
2) Read some BCs.
3) From those BCs, run the forward problem in order to get the input
   data for the CMM.
4) Run the CMM
5) Save the output, compare with the reference *T* field and same some
   diagnostic plots.

In real world applications, clearly some of the abovementioned steps
are not needed. Therefore, herenafter we also provide a test example
(`test13_real`) where the setting is much closer to a real case
application. Please use the script `run_cmm-real.py` to run this more
realistic test case.

data
    This folder contains the input data containing the Dirichlet BCs and some
    additional files that allow to shape the discretization domain.
template
    This folder contains a typical example of input JSON file that is used in all
    the following tests.
    
test01_c
    Setting to obtain Fig.3 of the companion paper. See there and in
    the JSON parameter file for more details.
    
test02_md_method
    Setting to obtain Fig.7 of the companion paper. See there and in
    the JSON parameter file for more details.
    
test03_md_nbd_OLD
    An old test. Results were not included in the companion paper.
    
test04_noise_OLD
    An old test. Results were not included in the companion paper.
    
test05_wells_OLD
    An old test. Results were not included in the companion paper.
    
test06_wells1a1
    A test where all the considered pumping wells are turned off/on
    one by one to implement the tomographic approach. Not included in
    the companion paper.

test07_md_paper
    Testing the tomographic approach with data with flow fields with
    diverse directions. See Fig.9 of the companion paper.
    
test08_noise
    Test to verify the robustness of the method when noise is added to the input data.
    
test09_manyiters
    This is just to test be behaviour of the CMM for many iterations.

test10_md_natural
    Tomogaphic approach with a multiple-flow setting which could be
    closer to the natural variability condition. See Appendix 1 of the
    companion paper.
    
test11_md_grad
   See the details on Appendix 2 of the companion paper (structured noise).
    
test12_md_grad_unstr
   See the details on Appendix 2 of the companion paper (structured noise).
   
test13_real
    This test case is provided as an example of a real case
    application of the method. Therefore, although the input data come
    from a syntetic field, all the other steps should be quite close
    to a real case study. The input data are the same used for
    `test10_md_natural`.
    For
    
   
   
