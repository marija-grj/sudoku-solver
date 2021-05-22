import numpy as np
from copy import deepcopy
from .utils import box_to_row

def swap_in_row(individual, puzzle):
    """Swap mutation within a random sudoku row

    Args:
        individual (Individual.representation): Potential sudoku solution
        puzzle (Individual.puzzle): Initial sudoku puzzle

    Returns:
        (array): Mutated Individual
    """
    # Get a random row to perform a mutation
    row = np.random.randint(0,9)
    # Get two mutation points in a random row.
    # Only for numbers that are not given as a puzzle (i.e. are zeros in the puzzle)
    mut_points = np.random.choice(np.where(puzzle[row] == 0)[0], 2)
    # Rename to shorten variable name
    i = individual

    i[row, mut_points[0]], i[row, mut_points[1]] = i[row, mut_points[1]], i[row, mut_points[0]]

    return i

def swap_in_column(individual, puzzle):
    """Swap mutation within a random sudoku column

    Args:
        individual (Individual.representation): Potential sudoku solution
        puzzle (Individual.puzzle): Initial sudoku puzzle

    Returns:
        (array): Mutated Individual
    """
    # Get a random column to perform a mutation
    col = np.random.randint(0,9)
    # Get two mutation points in a random column.
    # Only for numbers that are not given as a puzzle (i.e. are zeros in the puzzle)
    mut_points = np.random.choice(np.where(puzzle[:,col] == 0)[0], 2)
    # Rename to shorten variable name
    i = individual

    i[mut_points[0], col], i[mut_points[1], col] = i[mut_points[1], col], i[mut_points[0], col]

    return i

def swap_in_box(individual, puzzle):
    """Swap mutation within a random sudoku box

    Args:
        individual (Individual.representation): Potential sudoku solution
        puzzle (Individual.puzzle): Initial sudoku puzzle

    Returns:
        (array): Mutated Individual
    """
    # Get a random box to perform a mutation
    box = np.random.randint(0,9)
    # Get two mutation points in a random box.
    # Only for numbers that are not given as a puzzle (i.e. are zeros in the puzzle)
    mut_points = np.random.choice(np.where(box_to_row(puzzle)[box] == 0)[0], 2)
    # Rename to shorten variable name
    i = box_to_row(individual)

    i[box, mut_points[0]], i[box, mut_points[1]] = i[box, mut_points[1]], i[box, mut_points[0]]

    return box_to_row(i)

def uniform_one(individual, puzzle):
    """Uniform mutation for one random point

    Args:
        individual (Individual.representation): Potential sudoku solution
        puzzle (Individual.puzzle): Initial sudoku puzzle

    Returns:
        (array): Mutated Individual
    """
    # Get a random row to perform a mutation
    r, c = np.where(puzzle==0)
    i = np.random.randint(len(r))
    individual_m = deepcopy(individual)
    individual_m[r[i], c[i]] = np.random.choice(np.delete(np.arange(1,10), individual[r[i], c[i]]-1), 1)

    return individual_m
