import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError

    if vector.size != matrix.shape[1]:
        raise ShapeMismatchError

    if np.linalg.det(matrix) == 0:
        return None, None

    ans1 = (
        ((matrix @ vector) / np.linalg.norm(matrix, axis=1))[:, np.newaxis]
        * matrix
        / (np.linalg.norm(matrix, axis=1))[:, np.newaxis]
    )
    ans2 = vector - ans1
    return ans1, ans2
