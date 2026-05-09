import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    m, n = matrix.shape
    if m != n or n != vector.shape[0]:
        raise ShapeMismatchError
    if np.linalg.matrix_rank(matrix) != m:
        return None, None
    proj = ((matrix @ vector) / (np.linalg.norm(matrix, axis=-1) ** 2))[:, np.newaxis] * matrix
    return proj, vector - proj
