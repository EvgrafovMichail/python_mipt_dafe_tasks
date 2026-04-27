import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    M_vs, N = Vs.shape
    M_vj, K = Vj.shape

    if M_vs != M_vj or diag_A.shape[0] != K:
        raise ShapeMismatchError

    A = np.diag(diag_A)  # Диагональная матрица A
    Vj_H = Vj.conj().T  # Эмиртово сопряжение матрицы Vj
    composition = (Vj_H @ Vj) @ A  # Произведение матриц в скобке
    I_K = np.eye(K)
    revers_bracket = I_K + composition

    if np.linalg.det(revers_bracket) == 0:
        raise ShapeMismatchError

    Vj_H_Vs = Vj_H @ Vs
    right_summand = Vj @ (np.linalg.inv(revers_bracket) @ Vj_H_Vs)

    y = Vs - right_summand

    return y
