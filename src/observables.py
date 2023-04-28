import numpy as np

class observables(object):
#================================================================
# Class containing methods to find desired observables

    def __init__(self, J=1):
        #========================================================
        # Constructor that will define initial values of class

        self.J= J

    def totalEnergy(self, array):
        #========================================================
        # Find total ising energy of lattice

        arrayDown= np.roll(array, +1, axis= 0)
        arrayUp= np.roll(array, -1, axis=0)
        arrayRight= np.roll(array, +1, axis=1)
        arrayLeft= np.roll(array, -1, axis=1)
        latticeEnergy= -self.J*array*(arrayUp + arrayDown + arrayLeft + arrayRight)

        return latticeEnergy.sum()/2
    
    def totalMagnetisation(self, array):
        #========================================================
        # Find total magnetisiation of lattice

        return array.sum()
    
