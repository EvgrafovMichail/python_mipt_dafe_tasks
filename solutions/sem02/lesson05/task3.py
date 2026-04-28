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
    M = Vs.shape[0]
    K = diag_A.shape[0]
    Mj, Kj = Vj.shape
    if M != Mj:
        raise ShapeMismatchError
    if K != Kj:
        raise ShapeMismatchError
    A = np.diag(diag_A)
    VjH = Vj.conj().T
    inverted = np.linalg.inv(np.eye(K) + VjH @ Vj @ A)
    y = Vs - Vj @ inverted @ (VjH @ Vs)
    return y
