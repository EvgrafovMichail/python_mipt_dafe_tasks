import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    M_Vs, N = Vs.shape
    M_Vj, K = Vj.shape

    if M_Vs != M_Vj or diag_A.shape[0] != K:
        raise ShapeMismatchError

    Vj_H = Vj.conj().T
    A = np.diag(diag_A)

    y = Vs - Vj @ (np.linalg.inv(np.eye(K, dtype=complex) + Vj_H @ Vj @ A) @ (Vj_H @ Vs))

    return y
