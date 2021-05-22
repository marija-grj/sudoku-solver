import numpy as np
from charles.charles import Individual, Population
from data.sudoku_data import basic, easy
from charles.crossover import sp_co_row, sp_co_box, sp_co_column, sp_co_cell, tp_co_row, tp_co_column, tp_co_box, tp_co_cell
from charles.mutation import swap_in_row, swap_in_box, swap_in_column, uniform_one
from charles.selection import fps, tournament, rank
from matplotlib import pyplot as plt

def single_point(p1, p2):
    crossover = np.random.choice([sp_co_row, sp_co_column, sp_co_box, sp_co_cell], size=1)[0]
    return crossover(p1, p2)

def two_point(p1, p2):
    crossover = np.random.choice([tp_co_row, tp_co_column, tp_co_box, tp_co_cell], size=1)[0]
    return crossover(p1, p2)

def swap(individual, puzzle):
    mutation = np.random.choice([swap_in_row, swap_in_column, swap_in_box], size=1)[0]
    return mutation(individual, puzzle)

def random_co(p1, p2):
    crossover = np.random.choice([sp_co_row, sp_co_column, sp_co_box, sp_co_cell, tp_co_row, tp_co_column, tp_co_box, tp_co_cell], size=1)[0]
    return crossover(p1, p2)

def random_mu(individual, puzzle):
    mutation = np.random.choice([swap_in_row, swap_in_column, swap_in_box, uniform_one], size=1)[0]
    return mutation(individual, puzzle)

size=100
optim='max' 
puzzle=basic 
select=tournament
crossover=random_co
mutate=random_mu
co_prob=0.8
mu_prob=0.3

pop = Population(
    size=size, 
    optim=optim, 
    puzzle=puzzle
    )
fits = pop.evolve(
    gens=5, 
    select=select, 
    crossover=crossover,
    mutate=mutate, 
    co_prob=co_prob, 
    mu_prob=mu_prob,
    verbose=True
    )

plt.plot(range(1, len(fits)+1), 243-np.asarray(fits))
# plt.axhline(y = 243, color='r')
plt.title(f"Population: {size}, selection: {select.__name__},\ncrossover: {crossover.__name__}({co_prob}),\nmutation: {mutate.__name__}({mu_prob})")
plt.xlabel("Generation")
plt.ylabel("Loss")
plt.ylim(0)
plt.tight_layout()
plt.show()
