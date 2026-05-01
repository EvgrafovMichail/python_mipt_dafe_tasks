import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError("lhs and rhs must have same shape")

    return np.add(lhs, rhs)


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return 3 * (abscissa**2) + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs[0].shape != rhs[0].shape:
        raise ShapeMismatchError("lhs and rhs must have same shape")

    return np.sqrt(np.sum((lhs[:, np.newaxis] - rhs) ** 2, 2))
