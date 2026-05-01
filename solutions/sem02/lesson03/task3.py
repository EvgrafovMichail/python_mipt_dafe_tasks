import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.shape < (3,):
        raise ValueError
    indexs = np.arange(1, len(ordinates) - 1)
    sp_min = (ordinates[indexs] < ordinates[indexs - 1]) & (
        ordinates[indexs] < ordinates[indexs + 1]
    )
    sp_max = (ordinates[indexs] > ordinates[indexs - 1]) & (
        ordinates[indexs] > ordinates[indexs + 1]
    )
    return indexs[sp_min], indexs[sp_max]
