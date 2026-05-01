import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:

    if len(ordinates) < 3:
        raise ValueError

    diffs = np.diff(ordinates)
    mins = (diffs[:-1] < 0) & (diffs[1:] > 0)
    maxs = (diffs[:-1] > 0) & (diffs[1:] < 0)
    inners = np.arange(1, len(ordinates) - 1)
    min_inds = inners[mins]
    max_inds = inners[maxs]

    return (min_inds, max_inds)
