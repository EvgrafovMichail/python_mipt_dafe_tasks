import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.size:
        raise ShapeMismatchError
    if np.linalg.det(matrix) == 0:
        return (None, None)

    scalar_mult = matrix @ vector

    length = np.sum(matrix**2, axis=1)

    keff = (scalar_mult / length)[:, np.newaxis]

    projections = keff * matrix

    return (projections, vector - projections)
