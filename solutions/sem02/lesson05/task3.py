import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    if Vs.shape[0] != Vj.shape[0] or Vj.shape[1] != diag_A.size:
        raise ShapeMismatchError

    A = np.diag(diag_A)
    VHj = np.conj(Vj).T
    k = diag_A.size
    E = np.eye(k)
    pre_result_invert = np.linalg.inv(E + VHj @ Vj @ A)
    # в формуле раскрыты скобки и расставлены приоритеты,
    # чтобы уменьшить размер матрицы для конечного вычисления
    result = Vs - Vj @ pre_result_invert @ (VHj @ Vs)
    return result
