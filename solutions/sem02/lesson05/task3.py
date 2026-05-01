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

    M, N = Vs.shape
    M2, K = Vj.shape

    if M != M2 or len(diag_A) != K:
        raise ShapeMismatchError

    A = np.diag(diag_A)
    Vj_H = Vj.conj().T

    inner_inv = np.linalg.inv(np.eye(K) + Vj_H @ Vj @ A)
    return Vs - Vj @ inner_inv @ (Vj_H @ Vs)
