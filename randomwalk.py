import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import os
from shutil import rmtree

class RandomWalk:
    def __init__(self):
        self.run_num1 = 0
        self.run_num2 = 0
        self.run_num3 = 0
        
    def _save_plt(self, dim, run_num):
        if not os.path.exists(f'{dim}D-Plots'):
            os.mkdir(f'{dim}D-Plots')
            plt.savefig(f"{dim}D-Plots/{dim}D_run{run_num}")
            run_num += 1
        
    def clear_imgs(self, dimdirs=[1,2,3]):
        for dimdir in dimdirs:
            path = f'{dimdir}D-Plots'
            try:
                if os.path.exists(path) and os.path.isdir(path):
                    rmtree(path)
                    if dimdir == 1:
                        self.run_num1 = 0
                    elif dimdir == 2:
                        self.run_num2 = 0
                    else:
                        self.run_num3 = 0
                        
            except Exception:
                continue
    
    def _enforce_iter(self, obj):
            try:
                return tuple(obj)
            except TypeError as te:
                print(f"{obj} is not an iterable object - it is recommended to use a tuple for the starting coordinates")
    
    def one_dim(self, steps, sims=1, start=0, save=False):
        """Displays a plot on the screen of a one-dimensional random walk.

        Args:
            steps (int): Number of steps per simulation. 
                        1 step can go either forward or backward - i.e., +1 or -1 on a number line.
            sims (int, optional): Number of simulations to plot. Defaults to 1.
            start (int, optional): The starting position on the number-line. Defaults to 0.
            save (bool, optional): True to create a relevently named directory to save the image as a png to. Defaults to False.
        """
        
        for sim in range(sims): # each iteration is one run of the simulation
            next_coord = start # establish the next point on the coordinate line to go to
            coords = [(0, start)] # list of coords to unpack and plot - x= step number, y=current pos.
            
            for i in range(1, steps+1): # each iteration is one step of the current simulation
                next_coord += random.choice([-1, 1]) # either go forwards or backwards
                coords.append((i, next_coord)) # append the new coordinate 
        
            plt.plot(*zip(*coords), label=f"Simulation {sim}") # plot the sim.
        
        plt.title("1-D Random Walk")
        plt.ylabel("X-Position")
        plt.xlabel("Number of Steps")
        
        if save:
            self._save_plt(1, self.run_num1)
            
        plt.show()
        
        
        
    def two_dim(self, steps, sims=1, start=(0, 0), save=False):
        """Displays a plot on the screen of a two-dimensional random walk.

        Args:
            steps (int): Number of steps per simulation. 
                        1 step can either up, down, left or right on the coordinate plane.
            sims (int, optional): Number of simulations to plot. Defaults to 1.
            start (tuple, optional): Starting coordinates, formatted as (x, y). Defaults to (0, 0).
            save (bool, optional): True to create a relevently named directory to save the image as a png to. Defaults to False.
        """
        
        up, down, left, right = (0, 1), (0, -1), (-1, 0), (1, 0)
        directions = [up, down, left, right]
        
        start = self._enforce_iter(start)
        for sim in range(sims):
        
            next_coord = start
            coords = [start]
            
            for _ in range(1, steps+1):
                next_coord = tuple([sum(new_coord) for new_coord in zip(next_coord, random.choice(directions))])
                coords.append(next_coord)
    
            plt.plot(*zip(*coords), label=f"Simulation {sim}")
            
        plt.title("2-D Random Walk")
        plt.ylabel("Y-Position")
        plt.xlabel("X-Position")
        
        if save:
            self._save_plt(2, self.run_num2)
            
        plt.show()
        
        
    def three_dim(self, steps, sims=1, start=(0,0,0), save=False):
        """Displays a plot on the screen of a three-dimensional random walk.

        Args:
            steps (int): Number of steps per simulation.
                            A step is a single movement along the x, y, or z axis.
            sims (int, optional): Number of simulations to plot. Defaults to 1.
            start (tuple, optional): Starting coordinates, formatted as (x, y, z). Defaults to (0,0,0).
            save (bool, optional): True to create a relevently named directory to save the image as a png to. Defaults to False.
        """
        
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        
        left, right, forward, back, down, up = (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)
        directions = [left, right, forward, back, down, up]
        
        for sim in range(sims):
            
            next_coord = start
            coords = [start]
            
            for _ in range(1, steps+1):
                # pair up the x, y, and z of next_coord with a random step's x, y, z values. Sum the x's, then y's, then z's, make into new coordinate
                next_coord = tuple([sum(new_coord) for new_coord in zip(next_coord, random.choice(directions))])
                coords.append(next_coord)  
            ax.plot(*zip(*coords), label=f"Simulation {sim}")
            
        ax.set_title("3-D Random Walk")
        ax.set_ylabel("Y-Position")
        ax.set_xlabel("X-Position")
        ax.set_zlabel("Z-Position")
        ax.tick_params(labelsize="large")
        fig.set_size_inches(10,10)
  
        if save:
            self._save_plt(3, self.run_num3)
            
        plt.show()
