import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    left = ordinates[:-2]
    mid = ordinates[1:-1]
    right = ordinates[2:]

    max_e = (left < mid) & (mid > right)
    min_e = (left > mid) & (mid < right)
    ans = np.arange(1, ordinates.size - 1)

    return ans[min_e], ans[max_e]
