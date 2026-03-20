import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    Mj, K = Vj.shape
    Ms, N = Vs.shape
    A = np.diag(diag_A)
    Ka1, Ka2 = A.shape
    if Mj != Ms or Ka2 != K:
        raise ShapeMismatchError

    VjHT = Vj.conj().T
    VjHT_Vj = VjHT @ Vj
    I_ = np.eye(K)
    predres = I_ + VjHT_Vj @ A
    predres_inv = np.linalg.inv(predres)
    VjHT_Vs = VjHT @ Vs
    y = Vs - Vj @ (predres_inv @ VjHT_Vs)
    return y
