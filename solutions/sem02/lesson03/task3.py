import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError
    indices = np.arange(1, len(ordinates) - 1)

    inner = ordinates[1:-1]
    right = ordinates[2:]
    left = ordinates[:-2]
    local_maxes_mask = (inner > left) & (inner > right)
    local_mins_mask = (inner < left) & (inner < right)
    return (indices[local_mins_mask], indices[local_maxes_mask])
