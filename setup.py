import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmmpy",
    version="0.1.0",
    author="Alessandro Comunian",
    author_email="alessandro.comunian@unimi.it",
    description="Implementation of the Comparison Model Method",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://bitbucket.org/alecomunian/cmmpy",
    packages=setuptools.find_packages(where="cmmpy"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data = True,
    install_requires=[
        "numpy>=1.18.1",
        "pandas>=0.25.3",
        "matplotlib",
        "scipy",
        "flopy",
        "gstools",
        ],
    py_modules = ["tools", "cmm"],
)
