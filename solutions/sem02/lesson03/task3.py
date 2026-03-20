import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError
    else:
        idx = np.arange(ordinates.size)
        mask_def = (idx != 0) & (idx != ordinates.size - 1)
        idx = idx[mask_def]
        mask_min = (ordinates[idx] < ordinates[idx - 1]) & (ordinates[idx] < ordinates[idx + 1])
        mask_max = (ordinates[idx] > ordinates[idx - 1]) & (ordinates[idx] > ordinates[idx + 1])
        return tuple([idx[mask_min], idx[mask_max]])
