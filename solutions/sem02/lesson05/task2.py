import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError
    if matrix.shape[0] != vector.shape[0]:
        raise ShapeMismatchError
    if np.linalg.det(matrix) == 0:
        return (None, None)
    a = matrix @ vector.transpose()
    b = np.sum(matrix * matrix, axis=1)
    c1 = (a / b)[:, np.newaxis] * matrix
    c2 = vector - c1
    return (c1, c2)
