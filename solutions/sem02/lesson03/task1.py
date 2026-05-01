import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError

    return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return 3 * (abscissa**2) + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
):
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError
    n, m = lhs.shape
    k, c = rhs.shape

    dif = lhs.reshape(n, 1, m) - rhs.reshape(1, k, m)
    dis = np.sqrt(np.sum(dif**2, axis=2))

    return dis
