import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[1] != matrix.shape[0] or matrix.shape[0] != vector.size:
        raise ShapeMismatchError

    if np.linalg.det(matrix) == 0:
        return None, None

    scal = matrix @ vector.T
    share = scal / np.linalg.norm(matrix, axis=1) ** 2
    result1 = matrix * share.reshape(-1, 1)
    result2 = vector - result1

    return result1, result2
