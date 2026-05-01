import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    n = len(ordinates)
    if n < 3:
        raise ValueError
    
    ordinates_safe = ordinates[1:-1]
    
    max_mask = (ordinates_safe > ordinates[:-2]) & (ordinates_safe > ordinates[2:])
    min_mask = (ordinates_safe < ordinates[:-2]) & (ordinates_safe < ordinates[2:])
    indexes  = np.arange(1,n-1)
    
    ans = (indexes[min_mask], indexes[max_mask])
    
    return ans

