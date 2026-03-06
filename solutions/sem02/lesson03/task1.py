import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.size != rhs.size:
        raise ShapeMismatchError

    return np.add(lhs, rhs)


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return np.add(np.add(np.multiply(np.power(abscissa, 2), 3), np.multiply(abscissa, 2)), 1)


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError

    return np.sqrt(np.sum((lhs[:, None, :] - rhs[None, :, :]) ** 2, axis=2))
