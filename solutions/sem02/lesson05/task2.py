import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    m, n = matrix.shape
    if m != n:
        raise ShapeMismatchError
    if m != vector.shape[0]:
        raise ShapeMismatchError
    proections = []
    ortog_sost = []
    if np.linalg.det(matrix) == 0:
        return None, None
    else:
        scal_pr = vector @ matrix.T
        norm = np.linalg.norm(matrix, axis=1) ** 2
        koeff = scal_pr / norm
        proections = matrix * koeff[:, np.newaxis]
        ortog_sost = vector - proections
        return proections, ortog_sost

