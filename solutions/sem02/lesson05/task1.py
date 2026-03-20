import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if np.ndim(costs) != 2:
        raise ShapeMismatchError
    M, N = costs.shape
    if np.ndim(resource_amounts) != 1 or resource_amounts.size != M:
        raise ShapeMismatchError

    if np.ndim(demand_expected) != 1 or demand_expected.size != N:
        raise ShapeMismatchError

    resources_needed = np.sum(costs * demand_expected, axis=1)
    return all(resources_needed <= resource_amounts)
