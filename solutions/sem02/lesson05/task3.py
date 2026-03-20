import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if (
        Vs.ndim != 2
        or Vj.ndim != 2
        or diag_A.ndim != 1
        or Vs.shape[0] != Vj.shape[0]
        or Vj.shape[1] != diag_A.shape[0]
    ):
        raise ShapeMismatchError

    K = Vj.shape[1]

    VjH = Vj.conj().T
    A = np.diag(diag_A)

    E = np.eye(K, dtype=Vj.dtype)

    inner = E + VjH @ Vj @ A
    return Vs - Vj @ np.linalg.inv(inner) @ (VjH @ Vs)
