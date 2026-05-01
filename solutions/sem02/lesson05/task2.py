import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:

    if matrix.shape[1] != vector.shape[0] or matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError

    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return (None, None)

    scalar_mul = matrix @ vector
    squared_row_norms = np.sum(matrix * matrix, axis=1)
    coefs = scalar_mul / squared_row_norms

    projections = (matrix.transpose() * coefs).transpose()
    components = vector - projections
    return (projections, components)
