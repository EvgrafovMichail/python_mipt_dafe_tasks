import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[0] != vector.size:
        raise ShapeMismatchError

    n = matrix.shape[0]

    if np.linalg.matrix_rank(matrix) < n:
        return (None, None)

    scalar_prod = matrix @ vector  # скалярные произведения строк А (базисных векторов) на вектор a
    basis_len = np.sum(matrix * matrix, axis=1)  # квадраты длин базисных векторов
    coeffs = scalar_prod / basis_len  # коэффициенты проекций
    projections = coeffs[:, np.newaxis] * matrix  # проекции вектора на базисные вектора
    orth = vector - projections

    return projections, orth
