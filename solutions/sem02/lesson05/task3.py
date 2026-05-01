import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    M = Vs.shape[0]

    if Vj.shape[0] != M:
        raise ShapeMismatchError()
    if diag_A.shape[0] != Vj.shape[1]:
        raise ShapeMismatchError()
    K = Vj.shape[1]
    Vj_H = Vj.conj().T
    A = np.diag(diag_A)
    I_K = np.eye(K, dtype=complex)
    inner = np.linalg.solve(I_K + Vj_H @ Vj @ A, Vj_H @ Vs)
    y = Vs - Vj @ inner
    return y
