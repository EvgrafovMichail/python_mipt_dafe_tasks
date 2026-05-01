import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError("недостаточно элементов")

    local_maximums = np.array([], dtype=int)
    local_minimums = np.array([], dtype=int)

    for i in range(1, ordinates.size - 1):
        if ordinates[i] > ordinates[i - 1] and ordinates[i] > ordinates[i + 1]:
            local_maximums = np.append(local_maximums, i)
        elif ordinates[i] < ordinates[i - 1] and ordinates[i] < ordinates[i + 1]:
            local_minimums = np.append(local_minimums, i)

    return local_minimums, local_maximums
