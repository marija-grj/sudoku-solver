import numpy as np
from charles.charles import Individual, Population
from data.sudoku_data import basic, easy, hard
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


size=1500
optim='max' 
puzzle=hard 
select=tournament
crossover=two_point
mutate=uniform_one
mutation='uniform'
co_prob=0.7
mu_prob=0.01
fitness='unique_squared'

repetitions = 5
fits = [[] for _ in range(repetitions)]
for i in range(repetitions):
    pop = Population(
        size=size, 
        optim=optim, 
        puzzle=puzzle,
        fitness=fitness,
        mutation=mutation
    )
    fits[i] = pop.evolve(
        gens=100, 
        select=select, 
        crossover=crossover,
        mutate=mutate, 
        co_prob=co_prob, 
        mu_prob=mu_prob,
        verbose=False
        )
for i in range(5):
    if fitness == 'unique':
        plt.plot(range(1, len(fits[i])+1), (243-np.asarray(fits[i]))/216, alpha=0.5, color='steelblue')
    if fitness == 'unique_squared':
        plt.plot(range(1, len(fits[i])+1), (2187-np.asarray(fits[i]))/2160, alpha=0.5, color='steelblue')
    elif fitness == 'repetitions':
        plt.plot(range(1, len(fits[i])+1), np.asarray(fits[i])/216, alpha=0.5, color='steelblue')
# plt.axhline(y = 243, color='r')
plt.title(f"Population: {size}, selection: {select.__name__},\ncrossover: {crossover.__name__}({co_prob}),mutation: {mutate.__name__}({mu_prob}),\nfitness: {fitness}")
plt.xlabel("Generation")
plt.ylabel("Normalized loss")
plt.ylim(0)
plt.tight_layout()
plt.show()
