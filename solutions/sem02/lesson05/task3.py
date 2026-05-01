import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if diag_A.ndim != 1 or Vj.ndim != 2 or Vs.ndim != 2:
        raise ShapeMismatchError

    if Vj.shape[1] != len(diag_A) or Vj.shape[0] != Vs.shape[0]:
        raise ShapeMismatchError

    A = np.diag(diag_A)

    Vj_H = Vj.conj().T

    return Vs - Vj @ np.linalg.inv(np.eye(len(diag_A)) + Vj_H @ Vj @ A) @ (Vj_H @ Vs)
