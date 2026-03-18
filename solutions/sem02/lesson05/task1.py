import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    M, N = costs.shape
    if len(resource_amounts) != M:
        raise ShapeMismatchError
    if len(demand_expected) != N:
        raise ShapeMismatchError
    amount_resources_needed = np.sum(costs * demand_expected, axis=1)
    return all(amount_resources_needed <= resource_amounts)
