import matplotlib.pyplot as plt
import numpy as np

class animate(object):
#===========================================================
# Animate a simulation that returns an image without tying matplotlib to 
# simulation steps.

    def __init__(self, lattice_array, colourmap= 'magma'):
    #=======================================================
    # Initialise figure and inital frame of animation

        self.cmap= str(colourmap)
        self.fig= plt.figure()
        self.im= plt.imshow(lattice_array, animated=True, cmap= self.cmap)
        plt.colorbar()

    def draw_image(self, lattice_array):
    #=======================================================
    # Draw frame of the animation
        plt.clf()
        plt.cla()
        self.im= plt.imshow(lattice_array, animated= True, cmap= self.cmap)
        plt.colorbar()
        plt.draw()
        plt.pause(0.0001)


def main():
    #=======================================================
    # Test functionality of class   
    mean = (1, 2)
    cov = [[1, 0], [0, 1]]
    x= np.zeros((5,5))    
    animation= animate(x)
    
    for i in range(100):    
        x= np.random.choice(5, size=(5,5))
        animation.draw_image(x)

if __name__ == '__main__':
    main()