import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    left = ordinates[:-2]
    n = ordinates[1:-1]
    right = ordinates[2:]

    ordinates = np.arange(1, len(ordinates) - 1)

    mins = ordinates[((n < left) & (n < right))]
    maxs = ordinates[((n > left) & (n > right))]

    return mins, maxs
