import numpy as np


class ShapeMismatchError(Exception):
    pass


def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    N1, N2 = matrix.shape
    if N1 != N2 or N2 != len(vector):
        raise ShapeMismatchError

    if np.isclose(np.linalg.det(matrix), 0):
        return (None, None)

    # proj = []
    # ortog_comp = []

    # for e in matrix:
    #     projectoin = ((vector@e)/(e@e)*e)
    #     orth = vector - projectoin
    #     proj.append(projectoin)
    #     ortog_comp.append(orth)
    # return (np.array(projectoin), np.array(ortog_comp))

    coordinates = (matrix @ vector) / np.sum(matrix * matrix, axis=1)
    projections = coordinates[:, np.newaxis] * matrix
    orthogonals = vector - projections

    return (projections, orthogonals)
