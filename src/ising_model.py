"""
Script that will run ising model according to user defined temperature, lattice
size and algorithm
"""
import sys

def main():
    if len(sys.argv != 5):
        raise Exception('Run file in command line as ==>\npython3 ising_model.py [Lattice size] [Temperature] [Algorithm Type] [Simulation Type]')
    
    N=int(sys.argv[1]) 
    kT=float(sys.argv[2]) 
    algorithmType= str(sys.argv[3])
    simType= str(sys.argv[4])

    