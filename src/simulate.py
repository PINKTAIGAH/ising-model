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
        self.timestep= 0
        self.sweep= 1
       
        # 1 sweep ==> 2500 timesteps
        self.timestepLimit= 2500

        # Update visualisation every 10 sweeps
        self.visPeriod= 10
        

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

    def sweepUpdate(self):
        #========================================================
        # Update sweep value according to the current value of timestep variable

        if self.timestep == self.timestepLimit:
            self.sweep += 1
            self.timestep = 0
        
    def runGlauberSimulation(self):
        #========================================================
        # Run simulation of glauber algorithm with visualisation

        self.generateInitLattice()
        self.animation= animate(self.lattice)
        algorithmClass= algorithms(self.N, self.kT)
        while True:
            algorithmClass.glauberStep(self.lattice)
            self.timestep+=1
            self.sweepUpdate
            if self.sweep % self.visPeriod == 0:
                self.animation.draw_image(self.lattice)



