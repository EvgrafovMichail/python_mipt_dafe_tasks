import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,vector: np.ndarray,) -> tuple[np.ndarray | None, np.ndarray | None]:
    mshape = matrix.shape
    if not (mshape[0] == mshape[1] and mshape[0] == vector.size):
        raise ShapeMismatchError
    
    det = np.linalg.det(matrix)
    if abs(det) < 1e-10:
        return (None, None)
    
    ort_proj, ort_cond = [], []
    for base in matrix:
        ort_proj.append((base @ vector) * base / (np.linalg.norm(base) ** 2))
        ort_cond.append(vector - (base @ vector) * base / (np.linalg.norm(base) ** 2))
    return (np.array(ort_proj), np.array(ort_cond))