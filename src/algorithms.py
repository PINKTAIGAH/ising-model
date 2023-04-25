import numpy as np

class algorithms(object):
#================================================================
# Class containing all algorithms needed for the ising model for all algorithms

    def __init__(self, N, kT, algorithmType):
        
        self.N= N
        self.kT= kT

    def generateRandCoord(self):
        #=======================================================
        # Generate random indexes within lattice array bounds

        self.coords= np.random.randint(0, high= self.N, size= 2)
        
    
