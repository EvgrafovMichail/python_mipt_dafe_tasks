import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vj.shape[0] != Vs.shape[0] or Vj.shape[1] != diag_A.shape[0]:
        raise ShapeMismatchError

    Vjh = Vj.conj().T

    A = np.diag(diag_A)

    Ik = np.eye(diag_A.shape[0], dtype=np.uint8)

    jh_s_mul = Vjh @ Vs

    jh_j_mul = Vjh @ Vj

    inverted_sum = np.linalg.solve(Ik + jh_j_mul @ A, Ik)

    y = Vs - Vj @ inverted_sum @ jh_s_mul

    return y
