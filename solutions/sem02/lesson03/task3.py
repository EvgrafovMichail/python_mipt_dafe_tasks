import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    max_ind = (ordinates[:-2] < ordinates[1:-1]) & (ordinates[1:-1] > ordinates[2:])

    min_ind = (ordinates[:-2] > ordinates[1:-1]) & (ordinates[1:-1] < ordinates[2:])

    return np.where(min_ind)[0] + 1, np.where(max_ind)[0] + 1
