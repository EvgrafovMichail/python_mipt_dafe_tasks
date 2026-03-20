import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if (matrix.shape[0] != matrix.shape[1]) or (matrix.shape[1] != vector.shape[0]):
        raise ShapeMismatchError

    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return None, None

    proekziya = ((matrix @ vector) / (np.linalg.norm(matrix, axis=1) ** 2))[:, np.newaxis] * matrix

    return proekziya, vector - proekziya
