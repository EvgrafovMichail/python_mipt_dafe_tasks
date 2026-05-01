import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    left = ordinates[:-2]
    center = ordinates[1:-1]
    right = ordinates[2:]

    min_mask = (center < left) & (center < right)
    max_mask = (center > left) & (center > right)

    mins = np.where(min_mask)[0] + 1
    maxs = np.where(max_mask)[0] + 1

    return mins, maxs
