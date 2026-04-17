import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError
    diff = np.diff(ordinates)
    diff_next = diff[1:]
    diff_cur = diff[:-1]
    max_selection = (diff_cur > 0) & (diff_next < 0)
    min_selection = (diff_cur < 0) & (diff_next > 0)
    fin_max_idx = np.where(max_selection)[0] + 1
    fin_min_idx = np.where(min_selection)[0] + 1
    answer = (fin_min_idx, fin_max_idx)
    return answer



