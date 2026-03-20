import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError

    if np.linalg.slogdet(matrix)[0] == 0:
        return None, None

    scalar_prod = matrix @ vector
    module_sqrt = np.sum(matrix**2, axis=1)
    scalar_projection = scalar_prod / module_sqrt
    projection = scalar_projection[:, np.newaxis] * matrix

    return projection, vector - projection

