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
        for i in range(m):
            module = np.sum((matrix[i]) ** 2)
            pr_a_basis = (matrix[i] @ vector / module) * matrix[i]
            proections.append(pr_a_basis)
            ortog_sost.append(vector - pr_a_basis)
        return np.array(proections), np.array(ortog_sost)
