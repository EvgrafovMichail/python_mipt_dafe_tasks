import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    arr = np.arange(1, ordinates.size - 1)

    mask_minimums = (ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:])
    mask_maximums = (ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:])

    return arr[mask_minimums], arr[mask_maximums]
