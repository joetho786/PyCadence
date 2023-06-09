import os
def generate_ocn_script(values,default, init_file_path, output_file_path="simulation.ocn", output_log_path="output.txt"):
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
    f.close()
    rf.close()