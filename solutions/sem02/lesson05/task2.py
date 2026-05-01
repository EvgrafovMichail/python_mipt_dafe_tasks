import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError("размеры не согласованы ")

    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError("Матрица должна быть квадратной")

    if np.linalg.matrix_rank(matrix) < matrix.shape[1]:
        return None, None

    length = (matrix @ vector) / (np.linalg.norm(matrix, axis=1) ** 2)
    projection = matrix * length.reshape(-1, 1)
    ort = vector - projection
    return projection, ort
