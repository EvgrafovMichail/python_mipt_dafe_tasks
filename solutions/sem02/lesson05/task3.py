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
    Vjh = np.conj(Vj).transpose()
    A = np.diag(diag_A)
    almost_R_inv = np.linalg.inv(np.eye(Vj.shape[1]) + Vjh @ Vj @ A)
    return Vs - Vj @ (almost_R_inv @ (Vjh @ Vs))
