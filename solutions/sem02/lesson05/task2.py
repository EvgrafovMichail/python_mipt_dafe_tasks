import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    if matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError()
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError()

    if np.linalg.slogdet(matrix)[0] == 0:
        return (None, None)

    coef1 = matrix @ vector
    coef2 = np.sum(matrix**2, axis=1)
    coef = coef1 / coef2
    proekcii = matrix * coef[..., np.newaxis]
    ort_sost = vector - proekcii
    return (proekcii, ort_sost)
