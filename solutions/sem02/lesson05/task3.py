import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.shape[0] != Vj.shape[0]:
        raise ShapeMismatchError

    if Vj.shape[1] != diag_A.size:
        raise ShapeMismatchError

    Vjh = np.conj(Vj).T
    y = Vs - Vj @ np.linalg.solve(np.eye(Vj.shape[1]) + Vjh @ (Vj * diag_A), Vjh @ Vs)

    return y
