import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError
    diff1 = ordinates[1:] - ordinates[:-1]
    diff2 = -diff1[1:]
    diff1 = diff1[:-1]
    ans1 = (diff1 < 0) * (diff2 < 0)
    ans1 = ans1 * np.arange(1, ans1.size + 1)
    ans1 = ans1[ans1 != 0]
    ans2 = (diff1 > 0) * (diff2 > 0)
    ans2 = ans2 * np.arange(1, ans2.size + 1)
    ans2 = ans2[ans2 != 0]
    return ans1, ans2
