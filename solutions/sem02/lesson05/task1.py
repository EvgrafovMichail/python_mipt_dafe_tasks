import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape[0] != resource_amounts.shape[0] or costs.shape[1] != demand_expected.shape[0]:
        raise ShapeMismatchError("Shapes of input arrays do not match")

    total = costs @ demand_expected.reshape(-1, 1)
    return np.all(total <= resource_amounts.reshape(-1, 1))
