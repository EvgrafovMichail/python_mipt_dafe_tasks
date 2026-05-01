import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[1] != vector.shape[0] or matrix.shape[0] != vector.shape[0]:
        raise ShapeMismatchError

    if np.linalg.det(matrix) == 0:
        return None, None

    skal_stroka = vector @ matrix.T
    norms2 = np.sum(matrix**2, axis=1)

    coeffs = skal_stroka / norms2

    projections = matrix * coeffs[:, np.newaxis]

    ortogonal = vector - projections

    return projections, ortogonal
