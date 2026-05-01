import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vj.shape != (Vs.shape[0], diag_A.size):
        raise ShapeMismatchError

    K = Vj.shape[1]

    VjH = Vj.conj().T

    y = Vs - Vj @ np.linalg.inv(np.eye(K) + VjH @ Vj * diag_A) @ (VjH @ Vs)

    return y
