import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]: 
    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError
    
    n = matrix.shape[0]
    if len(vector) != n:
        raise ShapeMismatchError
    
    if abs(np.linalg.det(matrix)) < 1e-10:
        return None, None

    coeffs = np.linalg.solve(matrix.T, vector)
   
    projections = np.array([coeffs[i] * matrix[i] for i in range(n)])

    total_projection = np.sum(projections, axis=0)
    components = vector - total_projection
    
    return projections, components
