import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.shape[0] != Vj.shape[0]:
        raise ShapeMismatchError()
    if diag_A.shape[0] != Vj.shape[1]:
        raise ShapeMismatchError()

    M, K = Vj.shape
    A = np.diag(diag_A)
    Vjh = Vj.conj().T

    skobka = np.eye(K) + Vjh @ Vj @ A
    y = Vs - Vj @ np.linalg.solve(skobka, Vjh @ Vs)
    return y
