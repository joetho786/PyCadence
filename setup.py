from setuptools import setup, find_packages


def readall(path):
    with open(path) as fp:
        return fp.read()

setup(
    name="cadencepy",
    version="0.1.1",
    author="joetho786",
    author_email="thomas.2@iitj.ac.in",
    description="A python SDK for running simulation and reading data from Ocean Cadence",
    long_description=readall("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/joetho786/PyCadence",
    packages=find_packages(),
    package_data={'pycadence': ['*.sh']},
    install_requires=["requests","numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.6",
)

