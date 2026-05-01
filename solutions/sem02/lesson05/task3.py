import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.ndim != 2 or Vj.ndim != 2 or diag_A.ndim != 1:
        raise ShapeMismatchError

    if Vj.shape[0] != Vs.shape[0] or Vj.shape[1] != len(diag_A):
        raise ShapeMismatchError
    Vj_H = Vj.conj().T
    A = np.diag(diag_A)
    inner_matrix = np.eye(len(diag_A), dtype=complex) + Vj_H @ Vj @ A
    rhs = Vj_H @ Vs
    X = np.linalg.solve(inner_matrix, rhs)

    return Vs - Vj @ X
