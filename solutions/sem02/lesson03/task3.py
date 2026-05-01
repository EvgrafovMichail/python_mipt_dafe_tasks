import numpy as np


def get_extremum_indices(ordinates: np.ndarray,) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError
    maximum = (ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:])
    minimum = (ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:])

    maxima_inds = np.where(maximum)[0] + 1
    minima_inds = np.where(minimum)[0] + 1

    return (minima_inds, maxima_inds)