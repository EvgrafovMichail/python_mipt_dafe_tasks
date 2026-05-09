import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    m, n = costs.shape
    if resource_amounts.size != m or demand_expected.size != n:
        raise ShapeMismatchError
    new_costs = costs @ demand_expected.T
    return ((resource_amounts - new_costs) >= 0).all()
