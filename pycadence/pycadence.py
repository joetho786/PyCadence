import numpy as np
import subprocess
import os
import time


class Connector:
    def __init__(self, screen_name="ocean_simulation"):
        self.screen_name = screen_name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def disconnect(self):
        subprocess.call(["sh",self.dir_path+"/disconnect.sh", self.screen_name])
        if os.path.exists(self.dir_path+f"/{self.screen_name}.sh"):
            os.remove(self.dir_path+f"/{self.screen_name}.sh")
    
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
    
    def simulate(self,x,default, init_file_path, output_file_path="simulation.ocn", output_log_path="output.txt", read_output=read_output, fall_back_time=120):
        sim_status_log_path = f"sim_status_{self.screen_name}.txt"
        self.generate_ocn_script(x,default, init_file_path, output_file_path, output_log_path, sim_status_log_path)
        self.create_sh_file(output_file_path)
        if os.path.exists(sim_status_log_path):
            os.remove(sim_status_log_path)
        subprocess.call(["sh",self.dir_path+f"/{self.screen_name}.sh"])
        # read output file
        # if time in dead loop exceeds 10minutes system will kill the simulation
        start_time = time.time()
        # print(sim_status_log_path)
        while not os.path.exists(sim_status_log_path):
            if time.time() - start_time > fall_back_time:
                print("Simulation time out!")
                break
            pass
        data = read_output(output_log_path)
        return data

    def generate_ocn_script(self,values,default, init_file_path, output_file_path="simulation.ocn", output_log_path="output.txt", sim_status_log_path="sim_status.txt"):
        if not os.path.exists(init_file_path):
            AssertionError("init_file_path does not exist at the given path!")
        rf = open(init_file_path, "r")
        f = open(output_file_path, "w")
        lines = rf.readlines()
        p=0
        d=0
        l = len(values)
        ld = len(default)
        for line in lines:
            if "{value}" in line:
                f.write(line.replace("{value}", str(values[p]))) if p < l else f.write(line.replace("{value}", str(default[d])))
                p+=1
                d+=1
            elif "{output_log_path}" in line:
                f.write(line.replace("{output_log_path}", '"'+str(output_log_path)+'"'))
            else:
                f.write(line) 
    
        f.writelines(["\n",f"f = outfile(\"{sim_status_log_path}\",\"a\")\n","fprintf(f,\"completed\")\n","ocnCloseSession()\n"])
        f.close()
        rf.close()
    
    def create_sh_file(self, output_file_path="simulation.ocn"):
        f = open(self.dir_path+f"/{self.screen_name}.sh", "w")
        f.writelines(["#!/bin/bash\n","screen -r "+self.screen_name+" -X stuff "+"'load("+f'"{output_file_path}"'+")'"+"`echo -ne '\\015'`"])
        f.close()
        