"""
Script that will run ising model according to user defined temperature, lattice
size and algorithm
"""
import sys
from simulate import simulate

def main():
    if len(sys.argv != 4):
        raise Exception('Run file in command line as ==>\npython3 ising_model.py [Lattice size] [Temperature] [Algorithm Type]')
    
    N=int(sys.argv[1]) 
    kT=float(sys.argv[2]) 
    algorithmType= str(sys.argv[3])

    simulation= simulate(N, kT, algorithmType)

    if algorithmType == str('g'):
        simulation.runGlauberSimulation()


    