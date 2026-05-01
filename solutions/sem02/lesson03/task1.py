import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.size != rhs.size:
        raise ShapeMismatchError("размеры не совпадают ")

    return np.add(lhs, rhs)


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return np.add(
        np.add(np.multiply(np.multiply(abscissa, abscissa), 3), np.multiply(abscissa, 2)), 1
    )


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError("количество координат не совпадает")

    return np.sqrt(
        np.add(
            np.add(
                np.matmul(np.square(lhs).sum(axis=1, keepdims=True), np.ones((1, rhs.shape[0]))),
                np.matmul(np.ones((lhs.shape[0], 1)), np.square(rhs).sum(axis=1, keepdims=True).T),
            ),
            np.multiply(np.matmul(lhs, rhs.T), -2),
        )
    )
