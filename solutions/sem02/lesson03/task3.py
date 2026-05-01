import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError
    mask_max = (ordinates[:-2] < ordinates[1:-1]) & (ordinates[1:-1] > ordinates[2:])
    mask_min = (ordinates[:-2] > ordinates[1:-1]) & (ordinates[1:-1] < ordinates[2:])
    ind = np.arange(1, ordinates.size - 1)
    return tuple((ind[mask_min], ind[mask_max]))
