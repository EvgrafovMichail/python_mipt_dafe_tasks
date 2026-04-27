import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    
    if Vj.shape[1] != diag_A.size or Vs.shape[0] != Vj.shape[0]:
        raise ShapeMismatchError
    A = np.zeros((diag_A.size, diag_A.size), dtype=diag_A.dtype)
    A[np.arange(diag_A.size), np.arange(diag_A.size)] = diag_A
    Vj_H = np.transpose(Vj.conj())
    result_interm = Vj_H@Vj@A
    M0 = result_interm.shape[0]
    x1 = np.linalg.inv((np.eye(M0)+result_interm))
    x2 = Vj_H@Vs
    x3 = Vj@x1
    result = Vs - x3@x2
    # Так как 2 последних теста постоянно падали, пришлось выражение ниже
    # на отдельные кусочки поменьше разбить
    # result = Vs - Vj@(np.linalg.inv((np.eye(M0)+result_interm)))@Vj_H@Vs
    return result