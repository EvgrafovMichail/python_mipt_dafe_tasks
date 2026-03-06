import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.shape[0] < 3:
        raise ValueError

    indices = np.arange(1, ordinates.shape[0] - 1)
    prev = ordinates[indices - 1]
    curr = ordinates[indices]
    next = ordinates[indices + 1]

    min_mask = (curr < prev) & (curr < next)
    max_mask = (curr > prev) & (curr > next)

    return (indices[min_mask], indices[max_mask])
