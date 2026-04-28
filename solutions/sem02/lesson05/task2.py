import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError
    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return None, None
    scalar_products = matrix @ vector
    vector_square = np.sum(matrix**2, axis=1)
    projections = (matrix.T * scalar_products / vector_square).T
    components = vector - projections
    return projections, components
