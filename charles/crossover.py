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
    p1_flat = p1.box_to_row()
    p2_flat = p2.box_to_row()
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
    co_cel = np.random.randint(1, 9)
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
    cc = np.random.randint(1, 81, size=2)
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
    r_r = np.random.randint(1, 9)
    cc = np.random.randint(1, 9, size=2)
    offspring1 = p1.copy()
    offspring2 = p2.copy()
    # row-based two point crossover
    offspring1[r_r] = np.concatenate((offspring1[r_r][:cc.min()],offspring2[r_r][cc.min():cc.max()],offspring1[r_r][cc.max():]))
    p2[r_r] = np.concatenate((offspring2[r_r][:cc.min()],offspring1[r_r][cc.min():cc.max()],offspring2[r_r][cc.max():]))
    return offspring1, offspring2

def tp_co_column(p1, p2):
    """Implementation of two-point single column crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offsprings, resulting from the crossover.
    """
    r_c = np.random.randint(1, 9)
    cc = np.random.randint(1, 9, size=2)
    offspring1 = p1.copy()
    offspring2 = p2.copy()
    # col-based two point crossover
    offspring1[:,r_c] = np.concatenate((offspring1[:,r_c][:cc.min()],offspring2[:,r_c][cc.min():cc.max()],offspring1[:,r_c][cc.max():])).reshape(9, 1)
    offspring2[:,r_c] = np.concatenate((offspring2[:,r_c][:cc.min()],offspring1[:,r_c][cc.min():cc.max()],offspring2[:,r_c][cc.max():])).reshape(9, 1)
    return offspring1, offspring2

def tp_co_box(p1, p2):
    """Implementation of two-point single box crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offsprings, resulting from the crossover.
    """
    r_b = np.random.randint(1, 9)
    cc = np.random.randint(1, 9, size=2)
    # Convert parents' boxes into rows
    p1_flat = p1.box_to_row()
    p2_flat = p2.box_to_row()
    # Row-based two box crossover
    p1_flat[r_b] = np.concatenate((p1_flat[r_b][:cc.min()],p2_flat[r_b][cc.min():cc.max()],p1_flat[r_b][cc.max():]))
    p2_flat[r_b] = np.concatenate((p2_flat[r_b][:cc.min()],p1_flat[r_b][cc.min():cc.max()],p2_flat[r_b][cc.max():]))
    # Convert rows to back to boxes
    offspring1 = box_to_row(p1_flat)
    offspring2 = box_to_row(p2_flat)
    return offspring1, offspring2