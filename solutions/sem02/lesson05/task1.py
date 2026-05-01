import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.ndim != 2 or resource_amounts.ndim != 1 or demand_expected.ndim != 1:
        raise ShapeMismatchError()

    M, N = costs.shape
    if resource_amounts.shape[0] != M or demand_expected.shape[0] != N:
        raise ShapeMismatchError()

    resources_needed = costs @ demand_expected

    return bool(np.all(resources_needed <= resource_amounts))
