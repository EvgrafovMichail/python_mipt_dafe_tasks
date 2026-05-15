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
    return ((abscissa**2) * 3 + abscissa * 2) + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if len(lhs) != len(rhs):
        raise ShapeMismatchError

    return (np.sqrt(np.sum((lhs[:, np.newaxis, :] - rhs) ** 2, axis=2))).tolist()
