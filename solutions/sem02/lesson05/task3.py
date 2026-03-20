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

    Vj_h = np.conj(Vj).transpose()
    R_inv = np.linalg.inv(np.eye(Vj.shape[1]) + Vj_h @ Vj @ np.diag(diag_A))
    return Vs - Vj @ (R_inv @ (Vj_h @ Vs))
