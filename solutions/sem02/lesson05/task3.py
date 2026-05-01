import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:

    if Vs.ndim != 2 or Vj.ndim != 2 or diag_A.ndim != 1:
        raise ShapeMismatchError

    dim_M = Vs.shape[0]
    dim_K = diag_A.shape[0]
    dim_Mj, dim_Kj = Vj.shape
    if dim_M != dim_Mj:
        raise ShapeMismatchError

    if dim_K != dim_Kj:
        raise ShapeMismatchError

    marix_A = np.diag(diag_A)
    VjH = Vj.conj().transpose()
    matrix_E = np.diag(np.ones(dim_K))

    R_inv = np.linalg.inv(matrix_E + VjH @ Vj @ marix_A)

    y = Vs - Vj @ R_inv @ (VjH @ Vs)
    return y
