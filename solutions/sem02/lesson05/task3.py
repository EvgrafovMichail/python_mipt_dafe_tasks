import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(Vs: np.ndarray, Vj: np.ndarray, diag_A: np.ndarray) -> np.ndarray:
    if not (Vs.shape[0] == Vj.shape[0] and Vj.shape[1] == diag_A.shape[0]):
        raise ShapeMismatchError
    
    Vj_H = np.transpose(np.conj(Vj))
    A = np.diag(diag_A)
    I_K = np.eye(diag_A.size)

    return Vs - (Vj @ np.linalg.inv(I_K + Vj_H @ Vj @ A) @ (Vj_H @ Vs))
