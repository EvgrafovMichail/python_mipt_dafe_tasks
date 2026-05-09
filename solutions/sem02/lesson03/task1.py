import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.size != rhs.size:
        raise ShapeMismatchError
    return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return abscissa**2 * 3 + abscissa * 2 + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError
    lsq = (lhs**2) @ np.ones(shape=(lhs.shape[1], 1))
    rsq = np.ones(shape=(1, rhs.shape[1])) @ (rhs**2).T
    double = lhs @ rhs.T
    return np.sqrt(lsq - 2 * double + rsq)
