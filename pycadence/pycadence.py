import subprocess
import os
import time


class Connector:
    def __init__(self, screen_name="ocean_simulation", time_out = 120):
        self.screen_name = screen_name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.time_out = time_out
    
    def read_output(output_log_path):
        '''
        Helper function to parse the output file and return the data
        --------------------------------
        output_log_path: str
            path to the output file
        '''
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
            
        return data
    
    def simulate(self,x,default, init_file_path, output_file_path="simulation.ocn", output_log_path="output.txt", read_output=read_output):
        '''
        Function to run the simulation
        --------------------------------
        x: list
            list of values to be passed to the simulation
        default: list
            list of default values to be passed to the simulation
        init_file_path: str
            path to the template .ocn file to run the simulation
        output_file_path: str
            path to the temporary .ocn file to be created from the template. (Note: This file will be the one executed by the Ocean script)
        output_log_path: str
            path to the output file to store the simulation results
        read_output: function
            function to parse the output file and return the data
        '''
        sim_status_log_path = f"sim_status_{self.screen_name}.txt"
        self.generate_ocn_script(x,default, init_file_path, output_file_path, output_log_path)
        self.create_sh_file(output_file_path)

        if os.path.exists(sim_status_log_path):
            os.remove(sim_status_log_path)
        subprocess.call(["sh",self.dir_path+f"/{self.screen_name}.sh"])
       
        start_time = time.time()
    
        while not os.path.exists(sim_status_log_path):
            if time.time() - start_time > self.time_out:
                print("Simulation time out!")
                break
            pass
        while not os.path.exists(output_log_path):
            if time.time() - start_time > self.time_out:
                print("Simulation time out!")
                break
            pass

        data = read_output(output_log_path)
        return data

    def generate_ocn_script(self,values,default, init_file_path, output_file_path="simulation.ocn", output_log_path="output.txt"):
        '''
        Helper function to generate the .ocn file from the template
        --------------------------------
        values: list
            list of values to be passed to the simulation
        default: list
            list of default values to be passed to the simulation in case values are not provided
        init_file_path: str
            path to the template .ocn file to run the simulation
        output_file_path: str
            path to the temporary .ocn file to be created from the template. (Note: This file will be the one executed by the Ocean script)
        output_log_path: str
            path to the output file to store the simulation results

        '''
        sim_status_log_path = f"sim_status_{self.screen_name}.txt"
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
        f.writelines(["#!/bin/bash\n","tmux send-keys -t "+self.screen_name+"  "+"'load("+f'"{output_file_path}"'+")'"+" Enter"])
        f.close()
        