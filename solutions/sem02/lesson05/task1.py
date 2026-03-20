import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    M, N = costs.shape
    if resource_amounts.shape[0] != M or demand_expected.shape[0] != N:
        raise ShapeMismatchError

    for i in range(M):
        schet = 0
        for j in range(N):
            schet += costs[i, j] * demand_expected[j]
        if schet > resource_amounts[i]:
            return False
    return True
