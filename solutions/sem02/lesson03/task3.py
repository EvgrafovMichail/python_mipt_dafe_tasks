import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]: 
    
    if len(ordinates) < 3:
        raise ValueError
   
    left_compare = ordinates[1:-1] > ordinates[:-2]
    right_compare = ordinates[1:-1] > ordinates[2:] 
    
    max = left_compare & right_compare
    
    min = (~left_compare) & (~right_compare)
    
    max_indices = np.where(max)[0] + 1
    min_indices = np.where(min)[0] + 1
    
    return min_indices, max_indices
