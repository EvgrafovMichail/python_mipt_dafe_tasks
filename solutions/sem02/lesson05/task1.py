import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.size != resource_amounts.size * demand_expected.size:
        raise ShapeMismatchError
    spends = [0] * resource_amounts.size
    for j in range(demand_expected.size):
        amount = demand_expected[j]
        for i in range(resource_amounts.size):
            spends[i] += amount * costs[i][j]
    return np.all(spends <= resource_amounts)
