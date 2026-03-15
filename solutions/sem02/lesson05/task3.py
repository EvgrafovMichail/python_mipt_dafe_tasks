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
    I_k = np.eye(diag_A.size)
    Vj_H = (Vj.real - Vj.imag).T
    R__1 = np.linalg.inv((I_k + Vj @ A @ Vj_H))
    return R__1 @ Vs
