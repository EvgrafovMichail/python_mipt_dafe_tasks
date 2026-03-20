import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    m = Vs.shape[0]
    p, k = Vj.shape
    n = diag_A.size

    if m != p or n != k:
        raise ShapeMismatchError

    A = np.diag(diag_A)

    Vjh = np.transpose(np.conj(Vj))
    One = np.eye(k)

    return Vs - Vj @ (np.linalg.inv(One + (Vjh @ Vj) @ A)) @ (Vjh @ Vs)
