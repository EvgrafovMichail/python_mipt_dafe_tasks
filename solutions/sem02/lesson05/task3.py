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
    if len(diag_A) != Vj.shape[1]:
        raise ShapeMismatchError

    print(diag_A)
    Vjh = Vj.conj().T
    VjA = Vj * diag_A
    inn = np.eye(Vj.shape[1]) + Vjh @ VjA
    temp = np.linalg.inv(inn)
    y = Vs - Vj @ (temp @ (Vjh @ Vs))
    return y
