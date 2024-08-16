from setuptools import setup, find_packages

def readall(path):
    with open(path) as fp:
        return fp.read()

# if version already exists, then update the version in setup.py

from version import __version__

setup(
    name="CadenceConnector",
    version=__version__,
    author="joetho786",
    author_email="thomas.2@iitj.ac.in",
    description="A python SDK for running simulation and reading data from Ocean Cadence",
    long_description=readall("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/joetho786/PyCadence",
    packages=find_packages(),
    install_requires=["requests","numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.6",
)



