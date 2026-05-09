import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    m, n = Vs.shape
    k = diag_A.size
    if Vj.shape != (m, k):
        raise ShapeMismatchError
    Vh = Vj.conj().T
    matrix = np.eye(k) + (Vh @ Vj) * diag_A
    return Vs - Vj @ np.linalg.solve(matrix, Vh @ Vs)
