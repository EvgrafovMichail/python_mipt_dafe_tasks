import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.shape[0] < 3:
        raise ValueError

    left = ordinates[:-2]
    mid = ordinates[1:-1]
    right = ordinates[2:]

    minimums = (mid < left) & (mid < right)
    maximums = (mid > left) & (mid > right)

    indexes = np.arange(1, ordinates.shape[0] - 1)
    return indexes[minimums], indexes[maximums]
