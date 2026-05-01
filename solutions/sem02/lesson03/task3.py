import numpy as np

MIN_ELEM_COUNT = 3


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < MIN_ELEM_COUNT:
        raise ValueError
    left, x, right = ordinates[:-2], ordinates[1:-1], ordinates[2:]
    return (np.where((left > x) & (x < right))[0] + 1, np.where((left < x) & (x > right))[0] + 1)
