import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    rows, coloms = matrix.shape

    if rows != coloms:
        raise ShapeMismatchError
    if coloms != vector.size:
        raise ShapeMismatchError

    if np.linalg.matrix_rank(matrix) != rows:
        return (None, None)

    coeff = ((matrix @ vector) / np.sum(matrix**2, axis=1))[:, np.newaxis]
    projections = coeff * matrix
    components = vector - projections

    return projections, components
