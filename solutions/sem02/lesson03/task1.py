import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError()

    return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return (abscissa**2) * 3 + abscissa * 2 + 1


def get_mutual_l2_distances_vectorized(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
    if lhs.shape[0] != rhs.shape[0]:
        raise ShapeMismatchError()

    return np.array(
        [np.add.reduce(np.transpose((lhs[i] - rhs) ** 2)) ** 0.5 for i in range(len(lhs))]
    )
