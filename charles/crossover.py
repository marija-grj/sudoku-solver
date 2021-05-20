import numpy as np
from .utils import box_to_row

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
    co_box = np.random.randint(1, 9)
    # Convert parents' boxes into rows
    p1_flat = box_to_row(p1)
    p2_flat = box_to_row(p2)
    # Row-based single point crossover
    offspring1_flat = np.concatenate((p1_flat[:co_box], p2_flat[co_box:]), axis=0)
    offspring2_flat = np.concatenate((p2_flat[:co_box], p1_flat[co_box:]), axis=0)
    # Convert rows to back to boxes
    offspring1 = box_to_row(offspring1_flat)
    offspring2 = box_to_row(offspring2_flat)
    return offspring1, offspring2

def sp_co_cell(p1, p2):
    """Implementation of cell-based single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # return offspring1, offspring2