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

    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return (None, None)

    coefficients = matrix @ vector / np.linalg.norm(matrix, axis=1) ** 2

    ort_projections = matrix * coefficients[..., np.newaxis]

    normal_components = vector - ort_projections

    return (ort_projections, normal_components)
