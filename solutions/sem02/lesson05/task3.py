import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if np.ndim(Vs) != 2 or np.ndim(Vj) != 2 or np.ndim(diag_A) != 1:
        raise ShapeMismatchError

    if Vj.shape[0] != Vs.shape[0] or Vj.shape[1] != diag_A.size:
        raise ShapeMismatchError

    A = np.diag(diag_A)
    Vj_H = (Vj.real - 1j * Vj.imag).T
    R_1 = np.linalg.inv((np.eye(diag_A.size) + Vj_H @ Vj @ A))
    return Vs - Vj @ R_1 @ (Vj_H @ Vs)
