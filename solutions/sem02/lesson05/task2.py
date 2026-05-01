import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError
    if not np.linalg.det(matrix):
        return None, None
    scalar = matrix @ vector
    vector_square = np.sum(matrix**2, axis=1)
    projections = (matrix.T * scalar / vector_square).T
    components = vector - projections
    return projections, components
