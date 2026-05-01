import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] != vector.shape[0]:
        raise ShapeMismatchError

    if np.linalg.det(matrix) == 0:
        return None, None

    scalar_result = matrix @ vector
    lengths = np.sum(matrix**2, axis=1)
    projections = (scalar_result / lengths)[:, np.newaxis] * matrix
    return projections, vector - projections
