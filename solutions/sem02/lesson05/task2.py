import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    rows_count, column_count = matrix.shape
    if rows_count != column_count or column_count != vector.shape[0]:
        raise ShapeMismatchError
    if np.linalg.det(matrix) == 0:
        return None, None
    projection_coefficient = (np.sum((matrix * vector), axis=1) / np.sum((matrix**2), axis=1))[
        :, np.newaxis
    ]
    proj = projection_coefficient * matrix
    orth = vector - proj
    return proj, orth
