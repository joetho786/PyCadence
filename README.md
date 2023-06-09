# PyCadence
 A Python wrapper for running Cadence simulations

## Installation
1. Ocean Spectre and Python to be installed on the same device
2. Install PyCadence using pip
```pip install cadencepy```

## Usage
1. Make sure to have a template init.ocn file ready
2. In the ocn file placeholder values must be marked as {{value}} as shown in the sample init.ocn file placed in the sample folder
3. Create a screen with name ocean_simulation using the following shell command
```shell
screen -S ocean_simulation
```
4. Install and enable ocean terminal using the following shell commands
```shell
ocean
```
5. Then detach the screen using ctrl+a+d
6. Run the following python code to run the simulation
```python
import pycadence.pycadence as p
x = [1,2,3,4,5] # List of values to be substituted in the template
default = [1,2,3,4,5] # List of default values to be substituted in the template in case of error
p.simulate(x, default,"init.ocn","output.ocn","output.txt")
```
7. The result of simulation will be stored output.txt file and the output.ocn file will be the modified template file with the values substituted.
8. The simulate function also has an argument called read_output which takes a function as an argument. This function will be called after the simulation is complete and the output.txt file is generated. The function should take the output.txt file as an argument and return a dictionary of the values to be substituted in the template file. The following code shows an example of how to use this argument.
```python
import pycadence.pycadence as p
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

x = [1,2,3,4,5] # List of values to be substituted in the template
default = [1,2,3,4,5] # List of default values to be substituted in the template in case of error
p.simulate(x, default,"init.ocn","output.ocn","output.txt",read_output)
```
9. The above code will read the output.txt file and return a numpy array of the values to be substituted in the template file. The first column of the array will be substituted in the first placeholder and so on. The above code will work for any number of placeholders in the template file.