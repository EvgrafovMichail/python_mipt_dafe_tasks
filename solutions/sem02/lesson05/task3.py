import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    Vs = np.array(Vs)
    Vj = np.array(Vj)
    diag_A = np.array(diag_A)

    if Vs.ndim != 2 or Vj.ndim != 2 or diag_A.ndim != 1:
        raise ShapeMismatchError()

    M, N = Vs.shape
    M_vj, K = Vj.shape

    if M_vj != M or diag_A.shape[0] != K:
        raise ShapeMismatchError()

    I_K = np.eye(K)

    Vj_H = Vj.conj().T

    gram = Vj_H @ Vj
    inner = I_K + gram * diag_A
    rhs = Vj_H @ Vs
    solution = np.linalg.solve(inner, rhs)

    return Vs - Vj @ solution
