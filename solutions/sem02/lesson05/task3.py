import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    M, N = Vs.shape
    M2, K = Vj.shape
    if M != M2:
        raise ShapeMismatchError
    if len(diag_A) != K:
        raise ShapeMismatchError

    A = np.diag(diag_A)
    Vj_H = Vj.conj().T

    Vj_H_Vj = Vj_H @ Vj

    I_K = np.eye(K, dtype=Vj_H_Vj.dtype)
    inner = I_K + Vj_H_Vj @ A

    inner_inv = np.linalg.inv(inner)
    Vj_H_Vs = Vj_H @ Vs

    temp = inner_inv @ Vj_H_Vs

    y = Vs - Vj @ temp

    return y
