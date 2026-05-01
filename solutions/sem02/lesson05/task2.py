import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    M, N = matrix.shape

    if M != N:
        raise ShapeMismatchError
    if N != len(vector):
        raise ShapeMismatchError

    sign_det, _ = np.linalg.slogdet(matrix)
    if sign_det == 0:
        return (None, None)

    scalar_res = matrix @ vector
    norm_matrix_2 = np.sum(matrix**2, axis=1)
    ortogonal_proj_c = scalar_res / norm_matrix_2
    ortogonal_proj = ortogonal_proj_c[:, np.newaxis] * matrix
    ortogonal_parts = vector - ortogonal_proj

    return (ortogonal_proj, ortogonal_parts)
