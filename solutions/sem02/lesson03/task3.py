import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    left = ordinates[:-2]
    center = ordinates[1:-1]
    right = ordinates[2:]

    is_minimum = (center < left) & (center < right)
    is_maximum = (center > left) & (center > right)

    minimum_pos = np.where(is_minimum)[0] + 1
    maximum_pos = np.where(is_maximum)[0] + 1

    print(len(np.where(is_minimum)))

    return minimum_pos, maximum_pos


get_extremum_indices(np.array([0, 0, 1, 0]))
