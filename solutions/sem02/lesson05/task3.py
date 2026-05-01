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
    if Vj.shape[1] != np.diag(diag_A).shape[0] or Vj.shape[0] != Vs.shape[0]:
        raise ShapeMismatchError
    return Vs - Vj @ np.linalg.inv(
        np.eye(np.diag(diag_A).shape[0]) + np.conj(Vj).T @ Vj @ np.diag(diag_A)
    ) @ (np.conj(Vj).T @ Vs)
