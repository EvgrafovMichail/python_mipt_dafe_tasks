import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError
    if matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError
    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return None, None
    scalar_roduct = vector @ matrix.T
    norms_squared = np.sum(matrix * matrix, axis=1)
    coefficients = scalar_roduct / norms_squared
    projections = coefficients[:, np.newaxis] * matrix

    return projections, vector - projections
