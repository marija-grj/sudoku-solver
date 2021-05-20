import numpy as np
from charles.charles import Individual, Population
from data.sudoku_data import basic, easy
from charles.crossover import sp_co_row
from charles.mutation import swap_in_row
from charles.selection import fps, tournament, rank

pop = Population(
    size=200, 
    optim='max', 
    problem=basic
    )
pop.evolve(
    gens=100, 
    select=fps, 
    crossover=sp_co_row,
    mutate=swap_in_row, 
    co_prob=0.8, 
    mu_prob=0.3
    )