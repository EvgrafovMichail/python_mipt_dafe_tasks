import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError
    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return (None, None)
    dot = matrix @ vector
    norm_sq = np.sum(matrix**2, axis=1)
    coeff = dot / norm_sq
    proj = coeff.reshape(-1, 1) * matrix
    comp = vector - proj
    return (proj, comp)
