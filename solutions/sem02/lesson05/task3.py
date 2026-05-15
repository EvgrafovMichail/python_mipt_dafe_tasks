import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:

    Vj_H = Vj.conj().T

    M, K = Vj.shape

    if Vs.shape[0] != M:
        raise ShapeMismatchError

    if diag_A.size != K:
        raise ShapeMismatchError

    part_inner = np.eye(K, dtype=complex) + (Vj_H @ Vj) * diag_A
    part_inner_invert = np.linalg.inv(part_inner)
    part_out = part_out = Vj_H @ Vs
    y = Vs - Vj @ (part_inner_invert @ part_out)

    return y
