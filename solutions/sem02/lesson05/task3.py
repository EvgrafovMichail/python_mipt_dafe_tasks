import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    M, N = Vs.shape
    Mj, K = Vj.shape

    if M != Mj or K != len(diag_A):
        raise ShapeMismatchError

    Vj_H = (Vj.real - 1j * Vj.imag).T

    staples = np.eye(K) + (Vj_H @ Vj) * diag_A
    staples_inv = np.linalg.inv(staples)

    right_prod = Vj_H @ Vs

    return Vs - Vj @ (staples_inv @ right_prod)
