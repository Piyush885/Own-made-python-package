import math
import matplotlib.pyplot as plt
class Distribution():
    # Attributes-- mean, standard deviation, data.
    # Methods
    def __init__(self,mu=0,sigma = 1):
        self.mean = mu
        self.stdev = sigma
        self.data = []
        
    
    def read_data_file(self,file_name,sample=True):
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()        
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
        
    def plot_histogram(self):
        plt.hist(self.data)
        plt.title('Histogram on data')
        plt.xlabel('data')
        plt.ylabel('count')
    
    def pdf(self,x):
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
    # # Method Overriding----
    # def __add__(self,other):
    #     result = Distribution()
    #     result.mean = self.mean + other.mean
    #     result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
    #     return result


        
        
        