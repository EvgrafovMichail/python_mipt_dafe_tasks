import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError()
    if matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError()
    N = matrix.shape[0]
    if np.linalg.matrix_rank(matrix) < N:
        return None, None
    dots_av = matrix @ vector
    dots_vv = np.linalg.norm(matrix, axis=1) ** 2
    scalars = dots_av / dots_vv
    projections = scalars[:, np.newaxis] * matrix
    orthogonal_components = vector - projections

    return projections, orthogonal_components
