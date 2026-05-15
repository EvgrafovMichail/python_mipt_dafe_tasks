import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    num_left = ordinates[:-2]
    num_right = ordinates[2:]
    num = ordinates[1:-1]

    mask_max = (num > num_left) & (num > num_right)
    mask_min = (num < num_left) & (num < num_right)

    index_max = np.arange(1, len(ordinates) - 1)[mask_max]
    index_min = np.arange(1, len(ordinates) - 1)[mask_min]

    return index_min, index_max
