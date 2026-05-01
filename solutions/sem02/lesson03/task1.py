import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if len(lhs) != len(rhs):
        raise ShapeMismatchError
    return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return np.power(abscissa, 2) * 3 + abscissa * 2 + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError
    return [
        [
            sum((lhs[i][k] - rhs[j][k]) ** 2 for k in range(len(lhs[0]))) ** 0.5
            for j in range(len(rhs))
        ]
        for i in range(len(lhs))
    ]
