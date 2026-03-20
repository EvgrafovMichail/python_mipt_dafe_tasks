import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError()
    if matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError()

    if abs(np.linalg.det(matrix)) < 1e-10:
        return (None, None)

    dot = matrix @ vector
    norms_sq = np.sum(matrix * matrix, axis=1)
    coeffs = dot / norms_sq
    pr = coeffs[:, np.newaxis] * matrix
    ort = vector - pr

    return pr, ort
