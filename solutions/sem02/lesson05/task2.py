import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    matrix = np.array(matrix)
    vector = np.array(vector)

    if matrix.ndim != 2 or vector.ndim != 1:
        raise ShapeMismatchError()

    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError()

    N = matrix.shape[0]

    if vector.shape[0] != N:
        raise ShapeMismatchError()

    rank = np.linalg.matrix_rank(matrix)
    if rank < N:
        return (None, None)

    dots = matrix @ vector
    norm_sq = np.sum(matrix * matrix, axis=1)
    proj_coeffs = dots / norm_sq

    projections = proj_coeffs[:, None] * matrix
    components = vector - projections

    return (projections, components)
