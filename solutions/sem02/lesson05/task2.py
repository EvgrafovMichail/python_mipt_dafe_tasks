import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    rows, cols = matrix.shape

    if matrix.ndim != 2 or rows != cols or cols != len(vector):
        raise ShapeMismatchError

    det = np.linalg.det(matrix)
    if det == 0:
        return (None, None)

    numer = matrix @ vector
    square = np.sum(matrix**2, axis=1)
    coeff = numer / square
    projections = coeff.reshape(-1, 1) * matrix
    orthogonals = vector - projections

    return (projections, orthogonals)
