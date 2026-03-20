import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.shape[0] != Vj.shape[0] or Vj.shape[1] != diag_A.shape[0]:
        raise ShapeMismatchError("Shapes of input arrays do not match")

    return Vs - Vj @ np.linalg.inv(np.eye(Vj.shape[1]) + Vj.conj().T @ Vj @ np.diag(diag_A)) @ (
        Vj.conj().T @ Vs
    )
