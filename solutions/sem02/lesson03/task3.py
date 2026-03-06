import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    indexes = np.arange(len(ordinates))

    mask_max = (ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:])
    mask_min = (ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:])

    return indexes[1:-1][mask_min], indexes[1:-1][mask_max]
