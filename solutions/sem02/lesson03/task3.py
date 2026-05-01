import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    min_indices = (
        np.where((ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:]))[0] + 1
    )
    max_indices = (
        np.where((ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:]))[0] + 1
    )

    return (min_indices, max_indices)
