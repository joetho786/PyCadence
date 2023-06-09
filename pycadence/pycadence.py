import numpy as np
import subprocess
import os
import time
from .utils import generate_ocn_script

dir_path = os.path.dirname(os.path.realpath(__file__))

def connect():
    subprocess.call(["sh",dir_path+"/connect.sh"])

def disconnect():
    subprocess.call(["sh",dir_path+"/disconnect.sh"])

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

def simulate(x,default, init_file_path, output_file_path="simulation.ocn", output_log_path="output.txt", read_output=read_output):
    sim_status_log_path = "sim_status.txt"
    generate_ocn_script(x,default, init_file_path, output_file_path, output_log_path)
    if os.path.exists(sim_status_log_path):
        os.remove(sim_status_log_path)
    subprocess.call(["sh",dir_path+"/ocean_simulation.sh", output_file_path])
    # read output file
    # if time in dead loop exceeds 10minutes system will kill the simulation
    start_time = time.time()
    while not os.path.exists(sim_status_log_path):
        if time.time() - start_time > 120:
            print("Simulation time out!")
            break
        pass
    data = read_output(output_log_path)
    return data
