import numpy as np


def sp_co_row(p1, p2):
    """Implementation of row-based single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_row = np.random.randint(1, 9)
    offspring1 = np.concatenate((p1[:co_row], p2[co_row:]), axis=0)
    offspring2 = np.concatenate((p2[:co_row], p1[co_row:]), axis=0)
    return offspring1, offspring2

def sp_co_column(p1, p2):
    """Implementation of column-based single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_col = np.random.randint(1, 9)
    offspring1 = np.concatenate((p1[:,:co_col], p2[:,co_col:]), axis=1)
    offspring2 = np.concatenate((p2[:,:co_col], p1[:,co_col:]), axis=1)
    return offspring1, offspring2

def sp_co_box(p1, p2):
    """Implementation of box-based single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # return offspring1, offspring2

def sp_co_cell(p1, p2):
    """Implementation of cell-based single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # return offspring1, offspring2