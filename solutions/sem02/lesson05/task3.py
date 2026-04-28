import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:

    m = Vs.shape[0]
    k = Vj.shape[1]

    if m != Vj.shape[0] or k != diag_A.size:
        raise ShapeMismatchError

    Vjh = Vj.T.conj()
    return Vs - Vj @ np.linalg.inv(np.diag(np.ones(k)) + (Vjh @ Vj) * diag_A) @ (Vjh @ Vs)
