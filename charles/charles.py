import numpy as np
from operator import  attrgetter

class Individual:
    def __init__(self, problem, representation=None, initialization='random', fitness='unique'):
        np.random.seed()
        if type(problem) != np.ndarray:
            problem = np.asarray(problem)
        if type(representation) == np.ndarray:
            self.representation = representation
        elif representation == None:    
            if initialization == 'random':
                self.representation = np.where(problem > 0, problem, np.random.randint(1, 10, (9,9)))
        else:
            raise TypeError('Representation is not an numpy.ndarray nor None')
            
        if fitness == 'unique':
            self.fitness = self.evaluate_unique()
        self.problem = problem
    
    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value
    
    def transpose(self):
        return np.transpose(self.representation)
    
    def evaluate_unique(self):
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
    
    def __repr__(self):
        return f"Individual:\n{self.representation} \nFitness: {self.fitness}"
    

class Population:
    def __init__(self, size, optim, problem, initialization='random', fitness='unique'):
        self.individuals = []
        self.size = size 
        self.optim = optim # 'min' or 'max'
        self.problem = np.asarray(problem) # sudoku problem from sudoku_data: 'easy', 'hard', ...
        self.gen = 1
        for _ in range(size):
            self.individuals.append(
                Individual(
                    problem = problem,
                    initialization = initialization,
                    fitness = fitness
                )
            )
    
    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={self.size}, generation={self.gen})"
    
    def evolve(self, gens, select, crossover, mutate, co_prob, mu_prob):
        for gen in range(gens):
            new_pop = []
            while len(new_pop) < self.size:
                # Select parents
                parent1, parent2 = select(self), select(self)
                # Crossover with probability 'co_prob'
                if np.random.rand() < co_prob:
                    offspring1, offspring2 = crossover(parent1.representation, parent2.representation)
                else:
                    offspring1, offspring2 = parent1.representation, parent2.representation
                # Mutation with probability 'mu_prob'
                if np.random.rand() < mu_prob:
                    offspring1 = mutate(offspring1, problem=self.problem)
                if np.random.rand() < mu_prob:
                    offspring2 = mutate(offspring2, problem=self.problem)
                
                new_pop.append(Individual(representation=offspring1, problem=self.problem))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2, problem=self.problem))
                
            self.individuals = new_pop
            self.gen += 1
            
        if self.optim == "max":
            print(f'Best Individual: {max(self, key=attrgetter("fitness"))}; Goal: {(9*9*3)}')
        elif self.optim == "min":
            print(f'Best Individual: {min(self, key=attrgetter("fitness"))}; Goal: 0')
            
        print("Done")