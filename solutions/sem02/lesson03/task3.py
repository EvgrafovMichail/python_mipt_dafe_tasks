import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    indxs = np.arange(1, ordinates.size - 1)

    right = ordinates[indxs + 1]

    left = ordinates[indxs - 1]

    is_min = (ordinates[indxs] < left) & (ordinates[indxs] < right)
    is_max = (ordinates[indxs] > left) & (ordinates[indxs] > right)

    res_min = indxs[is_min]
    res_max = indxs[is_max]
    return res_min, res_max
