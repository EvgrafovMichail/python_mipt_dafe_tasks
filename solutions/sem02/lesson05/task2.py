import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if not all(np.array(matrix.shape) == np.array(vector.shape)):
        raise ShapeMismatchError

    if np.linalg.matrix_rank(matrix) < matrix.shape[0]:
        return (None, None)

    dot = matrix @ vector
    lenghts = np.linalg.norm(matrix, axis=1) ** 2

    matrix_proj = (dot / lenghts)[:, np.newaxis] * matrix

    matrix_sost = vector - matrix_proj

    return (matrix_proj, matrix_sost)
