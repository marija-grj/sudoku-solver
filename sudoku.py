import numpy as np
from charles.charles import Individual, Population
from data.sudoku_data import basic, easy
from charles.crossover import sp_co_row, sp_co_box, sp_co_column, sp_co_cell, tp_co_row, tp_co_column, tp_co_box, tp_co_cell
from charles.mutation import swap_in_row, swap_in_box, swap_in_column, uniform_one
from charles.selection import fps, tournament, rank

def single_point(p1, p2):
    crossover = np.random.choice([sp_co_row, sp_co_column, sp_co_box, sp_co_cell], size=1)[0]
    return crossover(p1, p2)

def two_point(p1, p2):
    crossover = np.random.choice([tp_co_row, tp_co_column, tp_co_box, tp_co_cell], size=1)[0]
    return crossover(p1, p2)

def swap(individual, puzzle):
    mutation = np.random.choice([swap_in_row, swap_in_column, swap_in_box], size=1)[0]
    return mutation(individual, puzzle)

pop = Population(
    size=100, 
    optim='max', 
    puzzle=basic
    )
pop.evolve(
    gens=20, 
    select=fps, 
    crossover=two_point,
    mutate=uniform_one, 
    co_prob=0.8, 
    mu_prob=0.3,
    verbose=True
    )

