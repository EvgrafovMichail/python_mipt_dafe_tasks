import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.ndim > 1 or len(ordinates) < 3:
        raise ValueError

    left = ordinates[:-2]
    center = ordinates[1:-1]
    right = ordinates[2:]

    max = (left < center) & (center > right)
    min = (left > center) & (center < right)

    index = np.arange(1, len(ordinates) - 1)

    return index[min], index[max]
