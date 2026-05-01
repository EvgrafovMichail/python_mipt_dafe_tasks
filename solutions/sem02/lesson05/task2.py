import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError
    if matrix.shape[1] != vector.size:
        raise ShapeMismatchError

    if np.linalg.det(matrix) == 0:
        return (None, None)

    orthogonal_projections = ((matrix @ vector) / (np.linalg.norm(matrix, axis=1) ** 2))[
        :, np.newaxis
    ] * matrix

    return orthogonal_projections, vector - orthogonal_projections
