import numpy as np


class ShapeMismatchError(Exception):
    pass


def adaptive_filter(
    Vs: np.ndarray,
    Vj: np.ndarray,
    diag_A: np.ndarray,
) -> np.ndarray:
    M, N = Vs.shape     
    M2, K = Vj.shape  
    
    if M != M2 or len(diag_A) != K:
        raise ShapeMismatchError

    Vj_H = Vj.conj().T
    
    A = np.diag(diag_A.astype(complex))

    I_K = np.eye(K, dtype=complex)
    matrix_to_invert = I_K + Vj_H @ Vj @ A

    inv_matrix = np.linalg.inv(matrix_to_invert)

    I_M = np.eye(M, dtype=complex)
    R_inv = I_M - Vj @ inv_matrix @ Vj_H

    y = R_inv @ Vs
    
    return y