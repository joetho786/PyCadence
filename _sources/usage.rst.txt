..  1. Make sure to have a template init.ocn file ready
.. 2. In the ocn file placeholder values must be marked as {{value}} as shown in the sample init.ocn file placed in the sample folder
.. 3. Go to the directory where the init.ocn file is placed and enable the Cadence environment using the following shell command
.. ```shell
..     csh
..     source /home/install/cshrc # Path to the cshrc file in the Cadence installation directory
.. ```
.. Next, create a new tmux session using the following shell command

.. ```shell
.. tmux new-session -s <session name>
.. ```
.. 4. Install and enable ocean terminal using the following shell commands
.. ```shell
.. ocean
.. ```
.. Now, The terminal can be detached or left running in the background. To detach the terminal, press Ctrl+b and then press d.

.. 6. Now, create a python script and use the following code to run the simulation

.. ```python
.. from pycadence.pycadence import Connector
.. x = [1,2,3,4,5] # List of values to be substituted in the template .ocn file
.. default = [1,2,3,4,5] # List of default values to be substituted in the template in case no value is provided
.. p=Connector(screen_name=<session name>)
.. p.simulate(x, default,"init.ocn","output.ocn","output.txt")
.. ```
.. 7. The result of simulation will be stored output.txt file and the output.ocn file will be the modified template file with the values substituted.
.. 8. The simulate function also has an argument called `read_output` which takes a function as an argument. This function will be called after the simulation is complete and the output.txt file is generated. The function should take the output.txt file as an argument and return a Iterable of the values parsed from the output.txt file. The following code demonstrates how to use the `read_output` argument.

.. ```python
.. from pycadence.pycadence import Connector
.. import numpy as np

.. def read_output(output_log_path):
..     with open(output_log_path, 'r+') as fp:
..         # read an store all lines into list
..         lines = fp.readlines()
..         data=[]
..         for line in lines[2:]:
..             try:
..                 temp = line.strip().split(" ")
..                 # print(temp)
..                 data.append([float(temp[0]),float(temp[-1])])
..             except Exception as e:
..                 # print("Error in reading output file")
..                 # print(e)
..                 pass
..         data = np.array(data)
..     return data

.. p=Connector(screen_name="ocean_simulation")
.. x = [1,2,3,4,5] # List of values to be substituted in the template
.. default = [1,2,3,4,5] # List of default values to be substituted in the template in case of error
.. p.simulate(x, default,"init.ocn","output.ocn","output.txt",read_output)
.. ```
.. 9. The above code will read the output.txt file and return a numpy array of the values.

.. 10. Refer to the init.ocn file in the sample folder for the template file format.



Usage
=====
1. Make sure to have a template \*.ocn file ready. 
2. In the ocn file placeholder values must be marked as {{value}} as shown in the sample init.ocn file placed in the sample folder.
.. note::
    A ocean script line writing the simulation results to a file should be present in the template file. Refer the sample init.ocn file in the sample folder for the same.

3. Go to the directory where the template *.ocn file is placed and enable the Cadence environment using the following shell command

.. code-block:: shell

    csh
    source /home/install/cshrc # Path to the cshrc file in the Cadence installation directory

Next, create a new tmux session using the following shell command

.. code-block:: shell

    tmux new-session -s <session name>

4. Install and enable ocean terminal using the following shell commands

.. code-block:: shell

    ocean

Now, The terminal can be detached or left running in the background. To detach the terminal, press Ctrl+b and then press d.

6. Now, create a python script and use the following code to run the simulation

.. code-block:: python

    from pycadence.pycadence import Connector
    import numpy as np

    x = [1,2,3,4,5] # List of values to be substituted in the template .ocn file
    default = [1,2,3,4,5] # List of default values to be substituted in the template in case no value is provided
    p=Connector(screen_name=<session name>)
    p.simulate(x, default,"init.ocn","output.ocn","output.txt")

7. The result of simulation will be stored output.txt file and the output.ocn file will be the modified template file with the values substituted.
8. The simulate function also has an argument called `read_output` which takes a function as an argument. This function will be called after the simulation is complete and the output.txt file is generated. The function should take the output.txt file as an argument and return a Iterable of the values parsed from the output.txt file. The following code demonstrates how to use the `read_output` argument.

    .. code-block:: python

        from pycadence.pycadence import Connector
        import numpy as np

        def read_output(output_log_path):
            with open(output_log_path, 'r+') as fp:
                # read an store all lines into list
                lines = fp.readlines()
                data=[]
                for line in lines[2:]:
                    try:
                        temp = line.strip().split(" ")
                        # print(temp)
                        data.append([float(temp[0]),float(temp[-1])])
                    except Exception as e:
                        # print("Error in reading output file")
                        # print(e)
                        pass
                data = np.array(data)
            return data

        p=Connector(screen_name="ocean_simulation")
        x = [1,2,3,4,5] # List of values to be substituted in the template
        default = [1,2,3,4,5] # List of default values to be substituted in the template in case of error
        p.simulate(x, default,"init.ocn","output.ocn","output.txt",read_output)

9. The above code will read the output.txt file using the `read_output` function and return a numpy array of the values.

