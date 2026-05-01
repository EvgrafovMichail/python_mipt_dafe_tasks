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
    return 3 * (abscissa**2) + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError

    scalar_product = lhs @ rhs.T
    lhs_sum_of_squares = np.add.reduce(lhs**2, axis=1)
    rhs_sum_of_squares = np.add.reduce(rhs**2, axis=1)

    return (
        lhs_sum_of_squares[:, np.newaxis] + rhs_sum_of_squares[np.newaxis, :] - 2 * scalar_product
    ) ** 0.5
