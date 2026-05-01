import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.ndim != 2:
        raise ShapeMismatchError

    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError

    if np.isclose(np.linalg.det(matrix), 0):
        return (None, None)

    scalar_mul = matrix @ vector

    len = np.linalg.norm(matrix, axis=-1)

    cos_a = scalar_mul / len**2

    proj = cos_a[:, np.newaxis] * matrix

    ort = vector - proj

    return (proj, ort)
