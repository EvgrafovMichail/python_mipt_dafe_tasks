import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    i, j = matrix.shape

    if i != j or vector.size != j:
        raise ShapeMismatchError

    if i != np.linalg.matrix_rank(matrix):
        return (None, None)

    lens = (np.linalg.norm(matrix, axis=1)) ** 2

    pros_norm = (matrix @ vector) / lens

    pros = pros_norm[..., np.newaxis] * matrix

    orts = vector - pros

    return pros, orts
