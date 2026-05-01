import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError

    # min_ordinates = []
    # max_ordinates = []
    # for i in range(1, len(ordinates)-1):
    #     if ordinates[i]<ordinates[i-1] and ordinates[i]<ordinates[i+1]:
    #         min_ordinates.append()
    #     elif ordinates[i]>ordinates[i-1] and ordinates[i]>ordinates[i+1]:
    #         max_ordinates.append(i)
    # return np.array(min_ordinates), np.array(max_ordinates)

    indexes = np.array(range(1, len(ordinates) - 1))

    left = ordinates[indexes - 1]
    right = ordinates[indexes + 1]
    current = ordinates[indexes]

    min_indx = indexes[(current < left) & (current < right)]
    max_indx = indexes[(current > left) & (current > right)]

    return min_indx, max_indx
