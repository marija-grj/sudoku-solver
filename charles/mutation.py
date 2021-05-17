from random import randint, sample

def swap_in_row(individual):
    """Swap mutation within a random sudoku row

    Args:
        individual (Individual): Potential sudoku solution

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points in a random row
    mut_points = ...
    
    # Rename to shorten variable name
    i = individual

    individual[mut_points[0]], individual[mut_points[1]] = i[mut_points[1]], i[mut_points[0]]

    return individual

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