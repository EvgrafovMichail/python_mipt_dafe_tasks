import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError
    
    left = ordinates[:-2]
    mid = ordinates[1:-1]
    right = ordinates[2:]

    mins = (left > mid) & (mid < right)
    maxes = (left < mid) & (mid > right)

    min_indices = np.where(mins)[0] + 1
    max_indices = np.where(maxes)[0] + 1

    return (min_indices, max_indices)
