import numpy as np
from operator import  attrgetter
from .utils import box_to_row, get_count

class Individual:
    def __init__(self, puzzle, representation=None, initialization='random', fitness='unique'):
        np.random.seed()
        if type(puzzle) != np.ndarray:
            puzzle = np.asarray(puzzle)
        if type(representation) == np.ndarray:
            self.representation = representation
        elif representation == None:    
            if initialization == 'random':
                self.representation = np.where(puzzle > 0, puzzle, np.random.randint(1, 10, (9,9)))
        else:
            raise TypeError('Representation is not an numpy.ndarray nor None')
            
        if fitness == 'unique':
            self.fitness = self.evaluate_unique()
        elif fitness == 'repetitions':
            self.fitness = self.evaluate_repetitions()
        elif fitness == 'unique_squared':
            self.fitness = self.evaluate_unique_sq()
        else:
            raise ValueError("Wrong fitness parameter value")
        self.puzzle = puzzle
    
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
        box_fitness = sum([len(set(row)) for row in box_to_row(self.representation)])
    
        return int(row_fitness + column_fitness + box_fitness)
    
    def evaluate_repetitions(self):
        """
        Sum of number of repeated numbers in each row, column and box. 
        Minimum (target) fitness is 0 (all numbers are unique), maximum fitness is 216 (all are the same).
        """
        row_fitness = sum([9-len(set(row)) for row in self.representation])
        column_fitness = sum([9-len(set(row)) for row in self.representation.transpose()])
        box_fitness = sum([9-len(set(row)) for row in box_to_row(self.representation)])
    
        return int(row_fitness + column_fitness + box_fitness)
    
    def evaluate_unique_sq(self):
        """
        Sum of squared number of unique numbers in each row, column and box. 
        Minimum fitness is 27 (all numbers are the same), maximum (target) fitness is 2187.
        """
        row_fitness = sum([len(set(row))**2 for row in self.representation])
        column_fitness = sum([len(set(row))**2 for row in self.representation.transpose()])
        box_fitness = sum([len(set(row))**2 for row in box_to_row(self.representation)])
    
        return int(row_fitness + column_fitness + box_fitness)
    
    def __repr__(self):
        return f"Individual:\n{self.representation} \nFitness: {self.fitness}"
    
    def flatten(self):
        return self.representation.flatten()
    
    def box_to_row(self):
        return box_to_row(self.representation)

class Population:
    def __init__(self, size, optim, puzzle, initialization='random', fitness='unique', mutation='swap'):
        """Initialize population
        
        Args:
            size:           size of the population [positive integer]
            optim:          type of optimization ['min','max']
            puzzle:         raw puzzle to be solved [nested list (9,9)]
            initialization: initialization function
            fitness:        fitness function ['unique'(def), 'unique_squared', 'repetitions']
            mutation:       mutation function ['swap'(def), 'unifirm']
        """
        self.individuals = []
        self.size = size 
        self.optim = optim # 'min' or 'max'
        self.puzzle = np.asarray(puzzle) # sudoku puzzle from sudoku_data: 'easy', 'hard', ...
        self.gen = 1
        self.fit_func = fitness
        self.mutation = mutation
        self.n = (np.asarray(self.puzzle) == 0).sum() # number of changeable elements (for uniform mutation)
        for _ in range(size):
            self.individuals.append(
                Individual(
                    puzzle = puzzle,
                    initialization = initialization,
                    fitness = fitness
                )
            )
    
    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={self.size}, generation={self.gen})"
    
    def evolve(self, gens, select, crossover, mutate, co_prob, mu_prob, verbose=False):
        """Evolve population
        
        Args:
            gens:       Number of generations to perform evolution for
            select:     Selection function
            crossover:  Crossover function
            mutate:     Mutation function
            co_prob:    Crossover probability
            mu_prob:    One element (cell if uniform mutation, row/column/box if swap mutation) mutation probability
            verbose:    Logging best individual of each generation
        """
        fitnesses = []
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
                if self.mutation == 'swap':
                    for i in range(get_count(p=mu_prob, n=27)):
                        offspring1 = mutate(offspring1, puzzle=self.puzzle)
                    for i in range(get_count(p=mu_prob, n=27)):
                        offspring2 = mutate(offspring2, puzzle=self.puzzle)
                if self.mutation == 'uniform':
                    for i in range(get_count(p=mu_prob, n=self.n)):
                        offspring1 = mutate(offspring1, puzzle=self.puzzle)
                    for i in range(get_count(p=mu_prob, n=self.n)):
                        offspring2 = mutate(offspring2, puzzle=self.puzzle)
                
                new_pop.append(Individual(representation=offspring1, puzzle=self.puzzle, fitness=self.fit_func))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2, puzzle=self.puzzle, fitness=self.fit_func))
                
            self.individuals = new_pop
            # Early stopping
            if self.optim == "max":
                best_fitness = max(self, key=attrgetter("fitness")).fitness
                fitnesses.append(best_fitness)
                if (self.fit_func == 'unique') & (best_fitness == 243):
                    break
                if (self.fit_func == 'unique_squared') & (best_fitness == 2187):
                    break
            elif self.optim == "min":
                best_fitness = min(self, key=attrgetter("fitness")).fitness
                fitnesses.append(best_fitness)
                if best_fitness == 0:
                    break
            
            self.gen += 1
            # Print logs if verbose is True
            if verbose: print(f'Generation {gen+2}, Best fitness: {max(self, key=attrgetter("fitness")).fitness}')
            
        if self.optim == "max":
            print(f'Generation: {self.gen} \nBest Individual: \n{max(self, key=attrgetter("fitness"))}; \nOptimization: max')
        elif self.optim == "min":
            print(f'Generation: {self.gen} \nBest Individual: \n{min(self, key=attrgetter("fitness"))}; \nOptimization: min')
            
        print("Done")
        return fitnesses