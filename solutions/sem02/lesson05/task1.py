import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape != (resource_amounts.size, demand_expected.size):
        raise ShapeMismatchError

    return np.all(np.sum(costs * demand_expected, axis=1) <= resource_amounts)
