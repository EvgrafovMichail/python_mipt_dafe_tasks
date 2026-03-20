import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError

    if np.linalg.matrix_rank(matrix) < matrix.shape[0]:
        return None, None

    dots = matrix @ vector
    norms = np.sum(matrix**2, axis=1)
    sc = dots / norms

    proj = sc[:, np.newaxis] * matrix
    ort = vector[np.newaxis, :] - proj

    return proj, ort
