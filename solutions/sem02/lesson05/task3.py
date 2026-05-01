import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if (Vs.shape[0] != Vj.shape[0]) or (Vj.shape[1] != diag_A.shape[0]):
        raise ShapeMismatchError

    A = np.diag(diag_A)
    E = np.eye(diag_A.shape[0])
    VjH = np.transpose(Vj.real - 1j * Vj.imag)

    return Vs - Vj @ np.linalg.inv(E + VjH @ Vj @ A) @ (VjH @ Vs)
