Examples
========

This wrapper lets us run any ADE-L simulation from Python. This enables us to run multiple algorithms, AI/ML models and optimization techniques
native to Python by encapsulating the ADE-L simulation as a function call with a return value. The use cases are:


    - Running multiple simulations with different parameters
    - Storing the results of the simulation in a structured format or directly loading into Python variables/arrays
    - Run AI/ML algorithms by using the simulation as just an objective function in Python
    - Allows for the use of various Python libraries for data analysis and visualization on the simulation results
    - This wrapper allows us to run simulations in jupyter notebooks and other Python environments

The following examples demonstrate how to use the PyCadence wrapper to run simulations from Python.

Example 1: Running a Monte Carlo simulation
-------------------------------------------

Consider a simple setup for a Monte Carlo simulation observing the phasenoise of a LC tank oscillator. The template ocn file generated is as follows.

.. literalinclude:: ./samples/init.ocn
    :language: ocean


The following Python code demonstrates how to run the simulation using the PyCadence wrapper. Note: it is just an example implementation.

.. literalinclude:: ./samples/example1.py
    :language: python
    


