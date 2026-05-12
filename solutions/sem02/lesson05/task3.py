import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    m, n = Vs.shape
    k = diag_A.size
    if Vj.shape != (m, k):
        raise ShapeMismatchError
    vjs = Vj.conj().T
    da = np.diag(diag_A)
    a = vjs @ Vj @ da
    vjvs = vjs @ Vs
    return Vs - Vj @ (np.linalg.inv(np.eye(k, dtype=complex) + a) @ vjvs)
