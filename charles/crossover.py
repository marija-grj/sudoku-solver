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
    h, w = p1.shape
    co_cel = np.random.randint(1, h)
    p1_flat,p2_flat = p1.flatten(),p2.flatten()
    child1_flat = np.concatenate((p1_flat[:,:co_cel],p2_flat[:,co_cel:]), axis = 1)
    child2_flat = np.concatenate((p2_flat[:,:co_cel],p1_flat[:,co_cel:]), axis = 1)
    offspring1 = child1_flat.reshape(h,w)
    offspring2 = child2_flat.reshape(h,w)
    return offspring1, offspring2

def tp_co_cell(p1,p2):
    h, w = p1.shape
    cpoints = np.random.randint(1, h*w, size=2)
    while cpoints[0] >= cpoints[1]:
        cpoints = np.random.randint(1, h*w, size=2)
    cpoint_1,cpoint_2 = cpoints[0],cpoints[-1]
    p1_flat,p2_flat = p1.flatten(),p2.flatten()
    child1_flat = p1_flat[:,:cpoint_1],p2_flat[:,cpoint_1:cpoint_2],p1_flat[:,cpoint_2:]
    child2_flat = p2_flat[:,:cpoint_1],p1_flat[:,cpoint_1:cpoint_2],p2_flat[:,cpoint_2:]
    child1_flat = np.hstack(child1_flat)
    child2_flat = np.hstack(child2_flat)
    offspring1 = child1_flat.reshape(h,w)
    offspring2 = child1_flat.reshape(h,w)
    return offspring1, offspring2