import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    left = ordinates[:-2]
    center = ordinates[1:-1]
    right = ordinates[2:]

    is_max = (center > left) & (center > right)
    is_min = (center < left) & (center < right)

    max_indexes = np.where(is_max)[0] + 1
    min_indexes = np.where(is_min)[0] + 1

    return min_indexes, max_indexes
