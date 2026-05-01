import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != len(vector):
        raise ShapeMismatchError

    if abs(np.linalg.det(matrix)) < 1e-10:
        return (None, None)

    lengths_sq = np.sum(matrix * matrix, axis=1)
    dots = np.sum(matrix * vector, axis=1)
    coeffs = dots / lengths_sq
    projs = np.zeros_like(matrix)

    for i in range(len(matrix)):
        projs[i] = coeffs[i] * matrix[i]

    components = vector - projs
    return (projs, components)
