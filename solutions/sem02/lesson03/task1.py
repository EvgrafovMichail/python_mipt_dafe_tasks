import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(lhs: np.ndarray, rhs: np.ndarray,) -> np.ndarray:
    if lhs.size != rhs.size:
        raise ShapeMismatchError
    result_array = lhs + rhs
    return result_array 


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray: 
    first_exp_array = abscissa.copy()
    second_exp_array = abscissa.copy()
    first_exp_array *= 2
    first_exp_array += 1
    second_exp_array **= 2
    second_exp_array *= 3
    return first_exp_array + second_exp_array


def get_mutual_l2_distances_vectorized(lhs: np.ndarray, rhs: np.ndarray,) -> np.ndarray: 
    if lhs.shape[1] != rhs.shape[1]:
        raise ShapeMismatchError
    result_matrix = lhs[:, np.newaxis, :] - rhs[np.newaxis, :, :]
    result_matrix **= 2
    result_matrix = np.sum(result_matrix, axis=2)
    result_matrix = np.sqrt(result_matrix)
    return result_matrix

