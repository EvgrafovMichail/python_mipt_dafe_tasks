import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or vector.size != matrix.shape[1]:
        raise ShapeMismatchError

    if np.linalg.det(matrix) == 0:
        return (None, None)

    scalar_matr_vect = np.sum(matrix * vector, axis=1)
    matr_squared = np.sum(matrix * matrix, axis=1)

    coef = (scalar_matr_vect / matr_squared).reshape(-1, 1)
    ort_projections = coef * matrix

    ort_components = vector - ort_projections
    return (ort_projections, ort_components)
