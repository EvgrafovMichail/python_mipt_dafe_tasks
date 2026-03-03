import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError
    lhs = ordinates[:-2]
    middle = ordinates[1:-1]
    rhs = ordinates[2:]
    ind = np.arange(1, ordinates.size - 1)
    mini = ind[(middle < lhs) & (middle < rhs)]
    maxi = ind[(middle > lhs) & (middle > rhs)]
    return (mini, maxi)