import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError

    result = np.zeros_like(lhs)
    for i in range(len(lhs)):
        result[i] = lhs[i] + rhs[i]

    return result


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    result = np.zeros_like(abscissa)

    for i in range(len(abscissa)):
        x = abscissa[i]
        x2 = x * x
        x3 = x2 * x
        result[i] = 2 * x3 + 3 * x2 + 5 * x + 7

    return result


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError

    n = lhs.shape[0]
    m = rhs.shape[0]
    d = lhs.shape[1]

    result = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            sum_squared = 0.0
            for k in range(d):
                raznost = lhs[i, k] - rhs[j, k]
                sum_squared += raznost * raznost
            result[i, j] = np.sqrt(sum_squared)

    return result
