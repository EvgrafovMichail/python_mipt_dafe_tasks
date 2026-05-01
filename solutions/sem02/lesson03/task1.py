import numpy as np


class ShapeMismatchError(Exception):
    pass


def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError
    return lhs + rhs


def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    # result = abscissa.copy()
    # result **= 2
    # result += abscissa *5
    # result += 1
    # return result
    return (abscissa**2) * 3 + abscissa * 2 + 1


def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if len(lhs[0]) != len(rhs[0]):
        raise ShapeMismatchError
    diff_coord = lhs[:, np.newaxis, :] - rhs[np.newaxis, :, :]
    summ_coord = np.sum(diff_coord**2, 2)
    return summ_coord**0.5
