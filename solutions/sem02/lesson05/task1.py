import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:

    first, second = costs.shape
    if demand_expected.size != second or resource_amounts.size != first:
        raise ShapeMismatchError

    costs_required = costs * demand_expected
    resource_required = np.sum(costs_required, axis = 1)
    result = resource_amounts - resource_required

    if np.all(result >= 0):
        return True
    
    return False