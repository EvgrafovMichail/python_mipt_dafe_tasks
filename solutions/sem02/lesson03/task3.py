import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    left = ordinates[:-2]
    mid = ordinates[1:-1]
    right = ordinates[2:]

    min_mask = (mid < left) & (mid < right)
    max_mask = (mid > left) & (mid > right)

    min_indices = np.where(min_mask)[0] + 1
    max_indices = np.where(max_mask)[0] + 1

    return min_indices, max_indices
