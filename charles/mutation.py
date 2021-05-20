from random import sample
import numpy as np

def swap_in_row(individual, problem):
    """Swap mutation within a random sudoku row

    Args:
        individual (Individual): Potential sudoku solution

    Returns:
        Individual: Mutated Individual
    """
    # Get a random row to perform a mutation
    row = np.random.randint(0,9)
    # Get two mutation points in a random row.
    # Only for numbers that are not given as a problem (i.e. are zeros in the problem)
    mut_points = np.random.choice(np.where(problem[row] == 0)[0], 2)
    # Rename to shorten variable name
    i = individual

    i[row, mut_points[0]], i[row, mut_points[1]] = i[row, mut_points[1]], i[row, mut_points[0]]

    return i

def swap_in_column(individual):
    """Swap mutation within a random sudoku column

    Args:
        individual (Individual): Potential sudoku solution

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points in a random column
    mut_points = ...
    
    # Rename to shorten variable name
    i = individual

    individual[mut_points[0]], individual[mut_points[1]] = i[mut_points[1]], i[mut_points[0]]

    return individual

def swap_in_box(individual):
    """Swap mutation within a random sudoku box

    Args:
        individual (Individual): Potential sudoku solution

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points in a random box
    mut_points = ...
    
    # Rename to shorten variable name
    i = individual

    individual[mut_points[0]], individual[mut_points[1]] = i[mut_points[1]], i[mut_points[0]]

    return individual