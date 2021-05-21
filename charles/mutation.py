import numpy as np
from .utils import box_to_row

def swap_in_row(individual, problem):
    """Swap mutation within a random sudoku row

    Args:
        individual (Individual.representation): Potential sudoku solution
        problem (Individual.problem): Initial sudoku problem

    Returns:
        (array): Mutated Individual
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

def swap_in_column(individual, problem):
    """Swap mutation within a random sudoku column

    Args:
        individual (Individual.representation): Potential sudoku solution
        problem (Individual.problem): Initial sudoku problem

    Returns:
        (array): Mutated Individual
    """
    # Get a random column to perform a mutation
    col = np.random.randint(0,9)
    # Get two mutation points in a random column.
    # Only for numbers that are not given as a problem (i.e. are zeros in the problem)
    mut_points = np.random.choice(np.where(problem[:,col] == 0)[0], 2)
    # Rename to shorten variable name
    i = individual

    i[mut_points[0], col], i[mut_points[1], col] = i[mut_points[1], col], i[mut_points[0], col]

    return i

def swap_in_box(individual, problem):
    """Swap mutation within a random sudoku box

    Args:
        individual (Individual.representation): Potential sudoku solution
        problem (Individual.problem): Initial sudoku problem

    Returns:
        (array): Mutated Individual
    """
    # Get a random box to perform a mutation
    box = np.random.randint(0,9)
    # Get two mutation points in a random box.
    # Only for numbers that are not given as a problem (i.e. are zeros in the problem)
    mut_points = np.random.choice(np.where(box_to_row(problem)[box] == 0)[0], 2)
    # Rename to shorten variable name
    i = box_to_row(individual)

    i[box, mut_points[0]], i[box, mut_points[1]] = i[box, mut_points[1]], i[box, mut_points[0]]

    return box_to_row(i)