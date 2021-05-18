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
        self.fitness = self.evaluate()
    
    # def __array__(self): 
    #     return np.array(self.representation)
    
    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value
    
    def transpose(self):
        return np.transpose(self.representation)
    
    def evaluate(self):
        """
        Sum of number of unique numbers in each row, column and box. 
        Minimum fitness is 27 (all numbers are the same), maximum (target) fitness is 243.
        """
        row_fitness = sum([len(set(row)) for row in self.representation])
        column_fitness = sum([len(set(row)) for row in self.representation.transpose()])
        # each of 9 boxes base coordinates (top left corner)
        box_base = [[x,y] for x in [0,3,6] for y in [0,3,6]] 
        # matrix where each row is flattened box content
        boxes_flattened = np.array([list(self.representation[b[0]:b[0]+3, b[1]:b[1]+3].flatten()) for b in box_base])
        box_fitness = sum([len(set(row)) for row in boxes_flattened])
    
        return int(row_fitness + column_fitness + box_fitness)
    
if __name__ == '__main__':
    ind = Individual(easy)
    draw(ind)
    print(f"Fitness: {ind.fitness}")
    