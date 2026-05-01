import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if not (Vs.shape[0] == Vj.shape[0] and Vj.shape[1] == diag_A.shape[0]):
        raise ShapeMismatchError
    return Vs - Vj @ np.linalg.inv(
        np.eye(diag_A.size) + np.transpose(np.conj(Vj)) @ Vj @ np.diag(diag_A)
    ) @ (np.transpose(np.conj(Vj)) @ Vs)
