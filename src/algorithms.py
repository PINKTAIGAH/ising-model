import numpy as np

class algorithms(object):
#================================================================
# Class containing all algorithms needed for the ising model for all algorithms

    def __init__(self, N, kT, J=1):
        #=======================================================
        # Constructor to define initial parameters of algorithm

        self.N= N
        self.kT= kT
        self.J= J

    def generateRandCoordGlauber(self):
        #=======================================================
        # Generate random indexes within lattice array bounds for glauber algorithm

        self.coords= np.random.randint(0, high= self.N, size= 2)

    def generateRandCoordKawasaki(self):
        #=======================================================
        # Generate random indexes within lattice array bounds for glauber algorithm

        self.coords1= np.random.randint(0, high= self.N, size= 2)
        self.coords2= np.random.randint(0, high= self.N, size= 2)
        
    def findDeltaEGlauber(self):
        #=======================================================
        # Find energy change between original and new state for glauber algorithm

        self.sCenter= self.array[self.coords]
        self.sCenterFlip= -self.sCenter

        initE= -self.J*self.sCenter*(np.roll(self.array, +1, axis=0)[self.coords] +\
                                         np.roll(self.array, -1, axis=0)[self.coords] +\
                                         np.roll(self.array, +1, axis=1)[self.coords] +\
                                         np.roll(self.array, -1, axis=1)[self.coords])       
        finalE= -self.J*self.sCenterFlip*(np.roll(self.array, +1, axis=0)[self.coords] +\
                                            np.roll(self.array, -1, axis=0)[self.coords] +\
                                            np.roll(self.array, +1, axis=1)[self.coords] +\
                                            np.roll(self.array, -1, axis=1)[self.coords])
        self.deltaE= finalE-initE

    def findDeltaEKawasaki(self):
        #=======================================================
        # Find energy change between original and new state for glauber algorithm

        self.sCenter1= self.array[self.coords1]
        self.sCenter2= self.array[self.coords2]

        initE= (-self.J*self.sCenter1*(np.roll(self.array[self.sCenter1], +1, axis=0) +\
                                       np.roll(self.array[self.sCenter1], -1, axis=0) +\
                                       np.roll(self.array[self.sCenter1], +1, axis=1) +\
                                       np.roll(self.array[self.sCenter1], -1, axis=1))) +\
               (-self.J*self.sCenter2*(np.roll(self.array[self.sCenter2], +1, axis=0) +\
                                       np.roll(self.array[self.sCenter2], -1, axis=0) +\
                                       np.roll(self.array[self.sCenter2], +1, axis=1) +\
                                       np.roll(self.array[self.sCenter2], -1, axis=1)))
        
        finalE= (-self.J*self.sCenter2*(np.roll(self.array[self.sCenter1], +1, axis=0) +\
                                       np.roll(self.array[self.sCenter1], -1, axis=0) +\
                                       np.roll(self.array[self.sCenter1], +1, axis=1) +\
                                       np.roll(self.array[self.sCenter1], -1, axis=1))) +\
               (-self.J*self.sCenter1*(np.roll(self.array[self.sCenter2], +1, axis=0) +\
                                       np.roll(self.array[self.sCenter2], -1, axis=0) +\
                                       np.roll(self.array[self.sCenter2], +1, axis=1) +\
                                       np.roll(self.array[self.sCenter2], -1, axis=1)))
        
        if (np.abs(self.coords1-self.coords2)==1).any():
            finalE+=2
            initE+=2
        
        self.deltaE= finalE - initE

    def applyChangeGlauber(self):
        #=======================================================
        # Apply the suggested change of the metropolis algorithm according to 
        # appropiate Boltzmann weights for glauber algorithm
        
        if self.deltaE <= 0:
            self.array[self.coords]= self.sCenterFlip

        elif np.random.rand < np.exp(-self.deltaE/self.kT):
            self.array[self.coords]= self.sCenterFlip

    def applyChangeKawasaki(self):
        #=======================================================
        # Apply the suggested change of the metropolis algorithm according to 
        # appropiate Boltzmann weights for kawasaki algorithm

        if self.deltaE <= 0:
            self.array[self.coords1]= self.sCenter2
            self.array[self.coords2]= self.sCenter1
        
        elif np.random.rand < np.exp(-self.deltaE/self.kT):
            self.array[self.coords1]= self.sCenter2
            self.array[self.coords2]= self.sCenter1

    def glauberStep(self, array):
        #========================================================
        # Apply one full cycle of the glauber algorithm to an array of the Ising 
        # model
        
        self.array= array
        self.generateRandCoordGlauber()
        self.findDeltaEGlauber()
        self.applyChangeGlauber()
        return self.array

    def kawasakiStep(self, array):
        #========================================================
        # Apply one full cycle of the kawasaki algorithm to an array of the Ising 
        # model   

        self.array= array
        self.generateRandCoordKawasaki()
        self.findDeltaEKawasaki()
        self.applyChangeKawasaki()   
        return self.array

        