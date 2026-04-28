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
    return 3 * abscissa**2 + 2 * abscissa + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError
    return (
        np.sum(
            (
                lhs.reshape(lhs.shape[0], 1, lhs.shape[1])
                - rhs.reshape(1, rhs.shape[0], rhs.shape[1])
            )
            ** 2,
            axis=2,
        )
        ** 0.5
    )
