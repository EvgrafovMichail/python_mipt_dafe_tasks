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

    firstVectorSq = np.sum(lhs**2, axis=1, keepdims=True)
    secondVectorSq = np.sum(rhs**2, axis=1, keepdims=True)
    scalarProducts = lhs @ rhs.T

    distances = np.sqrt(firstVectorSq + secondVectorSq.T - 2 * scalarProducts)

    return distances
