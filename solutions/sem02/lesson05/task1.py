import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.ndim != 2:
        raise ShapeMismatchError

    if costs.shape[0] != resource_amounts.shape[0] or costs.shape[1] != demand_expected.shape[0]:
        raise ShapeMismatchError

    max_amount = costs @ demand_expected

    return np.all(resource_amounts >= max_amount)
