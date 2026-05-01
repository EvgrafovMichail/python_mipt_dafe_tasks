import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    shp = matrix.shape
    if not (shp[0] == shp[1] and shp[0] == vector.size):
        raise ShapeMismatchError
    if not (np.linalg.matrix_rank(matrix) == shp[0]):
        return (None, None)
    proj, orth = [], []
    for base in matrix:
        proj.append((base @ vector) * base / (np.linalg.norm(base) ** 2))
        orth.append(vector - (base @ vector) * base / (np.linalg.norm(base) ** 2))
    return (np.array(proj), np.array(orth))
