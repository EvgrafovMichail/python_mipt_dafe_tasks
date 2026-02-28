import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray: ...


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray: ...


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray: ...
