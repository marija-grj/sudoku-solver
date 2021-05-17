from random import random
import numpy as np
from data.sudoku_data import easy
from charles.utils import draw

class Individual:
    def __init__(self, problem, initialization='random'):
        if type(problem) != 'numpy.array':
            problem = np.asarray(problem)
        if initialization == 'random':
            self.representation = np.where(problem > 0, problem, np.random.randint(1, 10, (9,9)))
    
    def __array__(self): 
        return np.array(self.representation)
    
if __name__ == '__main__':
    ind = Individual(easy)
    draw(np.array(ind))