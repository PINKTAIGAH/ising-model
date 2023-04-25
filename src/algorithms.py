import numpy as np

class algorithms(object):
#================================================================
# Class containing all algorithms needed for the ising model for all algorithms

    def __init__(self, N, kT, algorithmType):
        
        self.N= N
        self.kT= kT
        self.algorithmType= algorithmType
        
