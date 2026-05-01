import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError
    ind = np.arange(1, len(ordinates) - 1)
    return (
        ind[(ordinates[:-2] > ordinates[1:-1]) & (ordinates[1:-1] < ordinates[2:])],
        ind[(ordinates[:-2] < ordinates[1:-1]) & (ordinates[1:-1] > ordinates[2:])],
    )
