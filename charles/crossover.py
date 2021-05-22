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
    co_row = np.random.choice(9, 1)
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
    co_col = np.random.choice(9, 1)
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
    co_box = np.random.choice(9, 1)
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
    co_cel = np.random.choice(9, 1)
    p1_flat, p2_flat = p1.flatten(), p2.flatten()
    offspring1 = np.concatenate((p1_flat[:co_cel], p2_flat[co_cel:])).reshape(9, 9)
    offspring2 = np.concatenate((p2_flat[:co_cel], p1_flat[co_cel:])).reshape(9, 9)
    return offspring1, offspring2

def tp_co_cell(p1, p2):
    """Implementation of cell-based two point crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    cc = np.random.choice(81, 2 , replace= False)
    p1_flat, p2_flat = p1.flatten(), p2.flatten()
    offspring1 = np.concatenate((p1_flat[:cc.min()], p2_flat[cc.min():cc.max()], p1_flat[cc.max():])).reshape(9, 9)
    offspring2 = np.concatenate((p2_flat[:cc.min()], p1_flat[cc.min():cc.max()], p2_flat[cc.max():])).reshape(9, 9)
    return offspring1, offspring2

def tp_co_row(p1, p2):
    """Implementation of two-point single row crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offsprings, resulting from the crossover.
    """
    cc = np.random.choice(9, 2, replace= False)
    offspring1 = np.concatenate((p1[:cc.min()],p2[cc.min():cc.max()],p1[cc.max():]))
    offspring2 = np.concatenate((p2[:cc.min()],p1[cc.min():cc.max()],p2[cc.max():]))
    return offspring1, offspring2

def tp_co_column(p1, p2):
    """Implementation of two-point single column crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offsprings, resulting from the crossover.
    """
    cc = np.random.choice(9, 2, replace= False)
    offspring1 = np.concatenate((p1[:,:cc.min()],p2[:,cc.min():cc.max()],p1[:,cc.max():]), axis=1)
    offspring2 = np.concatenate((p2[:,:cc.min()],p1[:,cc.min():cc.max()],p2[:,cc.max():]), axis=1)
    return offspring1, offspring2

def tp_co_box(p1, p2):
    """Implementation of two-point single box crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offsprings, resulting from the crossover.
    """
    cc = np.random.choice(9, 2, replace= False)
    # Convert parents' boxes into rows
    p1_flat = box_to_row(p1)
    p2_flat = box_to_row(p2)
    # Row-based single point crossover
    offspring1_flat = np.concatenate((p1_flat[:cc.min()],p2_flat[cc.min():cc.max()],p1_flat[cc.max():]))
    offspring2_flat = np.concatenate((p2_flat[:cc.min()],p1_flat[cc.min():cc.max()],p2_flat[cc.max():]))
    # Convert rows to back to boxes
    offspring1 = box_to_row(offspring1_flat)
    offspring2 = box_to_row(offspring2_flat)
    return offspring1, offspring2