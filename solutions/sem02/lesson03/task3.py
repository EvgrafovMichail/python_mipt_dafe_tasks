import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError("ordinates is too small")

    indexes = np.arange(1, np.size(ordinates) - 1)
    l_value = ordinates[indexes - 1]
    r_value = ordinates[indexes + 1]

    return indexes[(ordinates[indexes] < l_value) & (ordinates[indexes] < r_value)], indexes[
        (ordinates[indexes] > l_value) & (ordinates[indexes] > r_value)
    ]
