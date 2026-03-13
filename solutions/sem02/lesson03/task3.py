import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError
    mask_for_maximums = (ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:])
    mask_for_minimums = (ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:])

    index_of_minimum = np.arange(1, len(ordinates) - 1)[mask_for_minimums]
    index_of_maximum = np.arange(1, len(ordinates) - 1)[mask_for_maximums]
    return index_of_minimum, index_of_maximum
