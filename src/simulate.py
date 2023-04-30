import numpy as np
from animate import Animate
from observables import Observables
from algorithms import Algorithms
from time import time

class Simulate(object):
#================================================================
# Class containing all algorithms needed for the ising model for all algorithms

    def __init__(self, N, kT, algType):
        #========================================================
        # Constructor that will define initial parameters of simulation

        self.N= N
        self.kT= kT
        self.algType= algType
        self.timestep= 0
        self.sweep= 0
       
        # 1 sweep ==> 2500 timesteps
        self.timestepLimit= self.N**2

        # Update visualisation every 10 sweeps
        self.visPeriod= 10
        
        self.observablesClass= Observables()
        self.wipeVisualisationData()

    def wipeVisualisationData(self):
        #========================================================
        # Wipe data from previous visualisation

        with open('../data/visualisationData.csv', 'w') as f:
            f.close()

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

    def updateVisualisation(self):
        #========================================================
        # Update visualisation according to update parameters
        
        if self.timestep % self.timestepLimit*self.visPeriod == 0:
            self.animation.drawImage(self.lattice)
            self.totalEnergy= self.observablesClass.totalEnergy(self.lattice)
            self.totalMagnetisation= self.observablesClass.totalMagnetisation(self.lattice)
            self.writeOutData()
            print(f'Time taken to update: {time() - self.t:.5} seconds')
            #print(f'Energy= {self.totalEnergy} #####  Magnetisation= {self.totalMagnetisation}')
        
    def writeOutData(self):
        #========================================================
        # Write energy and magnetisation data to file

        with open('../data/visualisationData.csv', 'ab') as f:
            #f.write(b'\n')
            np.savetxt(f, np.array([[self.sweep, self.totalEnergy, self.totalMagnetisation]]), delimiter= ',', fmt= '%d')
    
    def runGlauberSimulation(self):
        #========================================================
        # Run simulation of glauber algorithm with visualisation

        self.generateInitLattice()
        self.animation= Animate(self.lattice)
        algorithmClass= Algorithms(self.N, self.kT)
        while True:
            algorithmClass.glauberStep(self.lattice)
            self.timestep+=1
            self.t= time()
            if self.timestep % self.timestepLimit:
                self.sweep+= 1
            self.updateVisualisation()
            
    def runKawasakiSimulation(self):
        #========================================================
        # Run simulation of kawasaki algorithm with visualisation

        self.generateInitLattice()
        self.animation= Animate(self.lattice)
        algorithmClass= Algorithms(self.N, self.kT)
        while True:
            algorithmClass.kawasakiStep(self.lattice)
            self.timestep+=1
            self.t= time()
            self.updateVisualisation()        




