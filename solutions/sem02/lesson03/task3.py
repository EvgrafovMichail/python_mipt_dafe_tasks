import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    localMin = (ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:])
    min_indices = np.where(localMin)[0] + 1

    localMax = (ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:])
    max_indices = np.where(localMax)[0] + 1

    return (min_indices, max_indices)
