import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    first, second = matrix.shape

    if first != second or second != vector.size:
        raise ShapeMismatchError
    
    if np.linalg.det(matrix) == 0:
        return (None, None)
    
    vectors_from_matrix_sq_lens = np.sum(matrix**2, axis = 1)
    col_temp = np.sum(matrix*vector, axis = 1)
    col_temp = col_temp / vectors_from_matrix_sq_lens
    elem_1 = col_temp[:, np.newaxis] * matrix

    return (elem_1, vector - elem_1)
