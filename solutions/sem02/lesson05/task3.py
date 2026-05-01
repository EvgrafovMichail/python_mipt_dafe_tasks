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
        raise ShapeMismatchError()
    if diag_A.shape[0] != K:
        raise ShapeMismatchError()

    Vj_H = Vj.conj().T
    A = np.diag(diag_A)

    inner = np.eye(K) + Vj_H @ Vj @ A  # K K
    inner_inv = np.linalg.inv(inner)

    temp = Vj_H @ Vs  # K N
    temp = inner_inv @ temp  # K N
    temp = Vj @ temp  # M N

    y = Vs - temp

    return y
