import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.size != rhs.size:
        raise ShapeMismatchError
    else:
        return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return 3 * (abscissa**2) + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs[0].size != rhs[0].size:
        raise ShapeMismatchError
    else:
        lhs_new = lhs * np.ones((rhs.shape[0], 1, 1))
        rhs_new = np.transpose((rhs * np.ones((lhs.shape[0], 1, 1))), (1, 0, 2))
        return ((np.sum((lhs_new - rhs_new) ** 2, axis=2)) ** 0.5).T
