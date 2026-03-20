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

    if Vs.shape[0] != Vj.shape[0] or Vj.shape[1] != diag_A.size:
        raise ShapeMismatchError

    A = np.diag(diag_A)
    E = np.eye(diag_A.size)
    VjH = np.conj(Vj).T
    R_1 = np.linalg.inv(E + VjH @ Vj @ A)
    result = Vs - Vj @ R_1 @ (VjH @ Vs)

    return result
