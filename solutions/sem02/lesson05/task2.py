import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError

    if matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError

    if np.linalg.matrix_rank(matrix) != matrix.shape[0]:
        return (None, None)

    dot_pr = (matrix @ vector).reshape(-1, 1)
    abs_ma = abs(np.sum(matrix**2, axis=1)).reshape(-1, 1)
    ort_pr = (dot_pr / abs_ma) * matrix
    ort_comp = vector - ort_pr

    return (ort_pr, ort_comp)
