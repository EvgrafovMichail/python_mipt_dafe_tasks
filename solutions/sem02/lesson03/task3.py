import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    center = ordinates[1:-1]
    left = ordinates[:-2]
    right = ordinates[2:]

    extremum_min = (center < right) & (center < left)
    extremum_max = (center > right) & (center > left)

    range = np.arange(1, len(ordinates) - 1)

    return range[extremum_min], range[extremum_max]
