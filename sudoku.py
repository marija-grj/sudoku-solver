import numpy as np
from charles.charles import Individual, Population
from data.sudoku_data import basic, very_easy, easy, moderate, hard, very_hard
from charles.crossover import sp_co_row, sp_co_box, sp_co_column, sp_co_cell, tp_co_row, tp_co_column, tp_co_box, tp_co_cell
from charles.mutation import swap_in_row, swap_in_box, swap_in_column, uniform_one
from charles.selection import fps, tournament, rank
from matplotlib import pyplot as plt
import time

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
select=rank
crossover=two_point
mutate=swap
mutation='swap'
co_prob=0.7
mu_prob=0.01
fitness='unique'
elitism=[False, True]

repetitions = 5
param = ['no elitism','elitism']
fits = [[0 for _ in range(repetitions)] for _ in range(len(param))]
total = 0
start = time.time()
for i in range(len(param)):
    for r in range(repetitions):
        print(f"------{param[i]}-{r+1}------")
        
        pop = Population(
            size=size, 
            optim=optim, 
            puzzle=puzzle,
            fitness=fitness,
            mutation=mutation
        )
        fits[i][r] = pop.evolve(
            gens=100, 
            select=select, 
            crossover=crossover,
            mutate=mutate, 
            co_prob=co_prob, 
            mu_prob=mu_prob,
            elitism=elitism[i],
            verbose=False
            )
        stop = time.time()
        diff = stop - start
        start = stop
        total = total + diff
        print(f"Time: {round(total,4)} (+{round(diff, 4)})")
# print(fits)
colors = ['steelblue','lightcoral','darkseagreen']
for i in range(len(param)):
    for r in range(repetitions):
        if fitness == 'unique':
            plt.plot(range(1, len(fits[i][r])+1), (243-np.asarray(fits[i][r]))/216, alpha=0.5, color=colors[i])
        if fitness == 'unique_squared':
            plt.plot(range(1, len(fits[i][r])+1), (2187-np.asarray(fits[i][r]))/2160, alpha=0.5, color=colors[i])
        elif fitness == 'repetitions':
            plt.plot(range(1, len(fits[i][r])+1), np.asarray(fits[i][r])/216, alpha=0.5, color=colors[i])
# plt.axhline(y = 243, color='r')
plt.title(f"Population: {size}, selection: {select.__name__}, crossover: {crossover.__name__}({co_prob}),\nmutation: {mutate.__name__}({mu_prob}), fitness: {fitness},\n elitism: ['no','yes']")
plt.xlabel("Generation")
plt.ylabel("Normalized loss")
plt.ylim(0)
plt.tight_layout()
plt.show()
