import numpy as np


def get_extremum_indices(ordinates: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.shape[0] < 3:
        raise ValueError

    diff = np.diff(ordinates)
    signs = np.sign(diff)
    signs[signs == 0] = np.nan

    prev_sign = signs[:-1]
    next_sign = signs[1:]

    minima_mask = (prev_sign < 0) & (next_sign > 0)
    maxima_mask = (prev_sign > 0) & (next_sign < 0)

    return np.where(minima_mask)[0] + 1, np.where(maxima_mask)[0] + 1
