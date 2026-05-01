import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.shape[0] != Vj.shape[0] or Vj.shape[1] != diag_A.shape[0]:
        raise ShapeMismatchError

    Vhj = Vj.conj().T  # неуверен, что проходили этот метод, но не вижу другого способа
    B = np.eye(diag_A.size) + (Vhj @ Vj) * diag_A
    y = Vs - Vj @ np.linalg.solve(B, Vhj @ Vs)
    return y
