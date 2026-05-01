import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.shape[0] != Vj.shape[0] or Vj.shape[1] != diag_A.shape[0]:
        raise ShapeMismatchError

    Vj_h = np.transpose(np.conj(Vj))
    A = np.diag(diag_A)
    y = Vs - Vj @ np.linalg.inv(np.eye(Vj.shape[1]) + Vj_h @ Vj @ A) @ (Vj_h @ Vs)
    return y
