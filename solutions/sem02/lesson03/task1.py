import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray: 
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError
    return rhs+lhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray: 
    ans = 3 * (abscissa ** 2) + 2 * abscissa + 1
    return ans


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError
    
    return np.sqrt(np.sum((lhs[:, np.newaxis, :] - rhs[np.newaxis, :, :])**2, axis=2))
