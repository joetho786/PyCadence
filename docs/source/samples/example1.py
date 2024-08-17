from pycadence.pycadence import Connector
import numpy as np

p = Connector(screen_name="session1")

def generate_monte_carlo_samples( N, X):
    '''
    Function to generate monte carlo samples
    --------------------------------
    N: int
        number of samples to generate
    X: list
        list of default values of design variables
    '''
    lower_bound = X - 0.1*X
    upper_bound = X + 0.1*X

    samples=[]
    for i in range(len(lower_bound)):
        samples.append(np.random.uniform(lower_bound[i],upper_bound[i],N))  # Assumed variance of 10% of the mean
    samples=np.array(samples)
    return samples.T

def outputReader(output_log_path):
    '''
    Helper function to parse the output file and return the data. Customize this as per need with reference to the output file format.
    The default implementation can be found Connector().read_output()
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
        data = np.array(data)
    return data

def objective_function(x):
    '''
    Objective function to be optimized
    --------------------------------
    x: list
        list of values to be passed to the simulation
    '''
    default = [0.1, 0.1, 0.1, 0.1, 0.1] # some default values

    data = p.simulate(x,default, "init.ocn", "monte_simulation.ocn", "output.txt", read_output = outputReader)
    return data[54][1] # I am only interested in the 55th data point not the whole series. Note: This is just an example


if __name__ == "__main__":
    N = 1000 # number of samples
    X = [0.1, 0.1, 0.1, 0.1, 0.1] # default values of design variables
    samples = generate_monte_carlo_samples(N, X)
    evaluations = []
    for sample in samples:
        evaluations.append(objective_function(sample))
    evaluations = np.array(evaluations)
    print(evaluations)
    print("Mean: ", np.mean(evaluations))
    print("Variance: ", np.var(evaluations))
    print("Standard Deviation: ", np.std(evaluations))
    print("Max: ", np.max(evaluations))
    print("Min: ", np.min(evaluations))
    
    