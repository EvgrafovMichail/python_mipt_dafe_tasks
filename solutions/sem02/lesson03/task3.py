import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    prev = ordinates[:-2]
    curr = ordinates[1:-1]
    next = ordinates[2:]

    min_mask = (curr < prev) & (curr < next)
    max_mask = (curr > prev) & (curr > next)

    indices = np.arange(1, len(ordinates) - 1)

    min_index = indices[min_mask]
    max_index = indices[max_mask]

    return (min_index, max_index)
