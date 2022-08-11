import math
from unittest import result
from .Distribution import Distribution

# Gaussian class

class Gaussian(Distribution):
    def __init__(self,mu=0,sigma=1):
        Distribution.__init__(self,mu,sigma)
        
    def calculate_mean(self):
        self.mean = sum(self.data)/len(self.data)
        return self.mean
    def calculate_stdev(self,sample = True):
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
    
        mean = self.mean
    
        sigma = 0
    
        for d in self.data:
            sigma += (d - mean) ** 2
        
        sigma = math.sqrt(sigma / n)
    
        self.stdev = sigma
        
        return self.stdev
    def __add__(self,other):
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        return result

		

	