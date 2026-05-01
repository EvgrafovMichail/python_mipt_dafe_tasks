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

    A = np.diag(diag_A)

    if Vj.shape[1] != A.shape[0] or Vj.shape[0] != Vs.shape[0]:
        raise ShapeMismatchError

    Vj_H = (Vj.real - 1j * Vj.imag).T
    return Vs - Vj @ np.linalg.inv(np.eye(A.shape[0]) + Vj_H @ Vj @ A) @ (Vj_H @ Vs)
