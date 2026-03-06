import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    array1 = np.arange(1, len(ordinates) - 1)
    index0 = array1 - 1
    index2 = array1 + 1
    max_condition = (ordinates[index0] < ordinates[array1]) & (
        ordinates[array1] > ordinates[index2]
    )
    maxs = array1[max_condition]
    min_condition = (ordinates[index0] > ordinates[array1]) & (
        ordinates[array1] < ordinates[index2]
    )
    mins = array1[min_condition]

    return (mins, maxs)
