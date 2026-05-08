import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if resource_amounts.shape[0] != costs.shape[0] or demand_expected.shape[0] != costs.shape[1]:
        raise ShapeMismatchError
    total = costs @ demand_expected
    check = total <= resource_amounts
    return all(check)
