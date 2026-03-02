import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    indexes = np.arange(1, ordinates.size - 1)
    lhs = ordinates[indexes - 1]
    rhs = ordinates[indexes + 1]
    minimals = indexes[(ordinates[indexes] < lhs) & (ordinates[indexes] < rhs)]
    maximals = indexes[(ordinates[indexes] > lhs) & (ordinates[indexes] > rhs)]

    return minimals, maximals
