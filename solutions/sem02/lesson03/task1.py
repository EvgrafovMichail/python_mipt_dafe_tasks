import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if np.size(lhs) != np.size(rhs):
        raise ShapeMismatchError
    return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return 3 * (abscissa**2) + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if np.size(lhs, 1) != np.size(rhs, 1):
        raise ShapeMismatchError
    dist = lhs[:, np.newaxis, :] - rhs[np.newaxis, :, :]
    return np.sqrt(np.sum(dist**2, 2))
