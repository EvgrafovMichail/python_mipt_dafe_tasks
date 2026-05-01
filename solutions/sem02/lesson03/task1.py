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
    return 3 * abscissa**2 + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError

    lhs_squared = np.sum(lhs**2, axis=1).reshape(-1, 1)
    rhs_squared = np.sum(rhs**2, axis=1).reshape(1, -1)
    cross_term = np.dot(lhs, rhs.T)

    return np.sqrt(lhs_squared - 2 * cross_term + rhs_squared)
