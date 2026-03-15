import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError

    if matrix.shape[1] != vector.size:
        raise ShapeMismatchError

    if not np.linalg.det(matrix):
        return None, None

    scalars = matrix @ vector
    norms = np.linalg.norm(matrix, axis=1)
    projections = matrix * scalars[..., np.newaxis] / norms[..., np.newaxis] ** 2
    components = vector - projections
    return projections, components
