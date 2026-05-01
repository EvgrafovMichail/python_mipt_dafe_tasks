import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    M, N = costs.shape
    
    if len(resource_amounts) != M or len(demand_expected) != N:
        raise ShapeMismatchError

    return bool(np.all(costs @ demand_expected <= resource_amounts))