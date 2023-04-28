import numpy as np
from animate import animate
from algorithms import algorithms

class simulate(object):
#================================================================
# Class containing all algorithms needed for the ising model for all algorithms

    def __init__(self, N, kT, algType):
        #========================================================
        # Constructor that will define initial parameters of simulation

        self.N= N
        self.kT= kT
        self.algType= algType

    def generateInitLattice(self):
        #========================================================
        # Generate inital lattice with equal probability spins

        self.lattice= np.random.choice(np.array([1,-1]), size=(self.N, self.N))
    
    def generateInitLatticeGlauberEq(self):
        #========================================================
        # Generate inital lattice with spis alliged near steady state for Galuber
        # algorithm

        self.lattice= np.ones((self.N, self.N))

    def generateInitLatticeKawasakiEq(self):
        #========================================================
        # Generate inital lattice with spis alliged near steady state for Galuber
        # algorithm

        self.lattice= np.ones((self.N, self.N))
        self.lattice[int(self.N/4):int(3*self.N/4), int(self.N/4):int(3*self.N/4)]= -1

