import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if (
        costs.ndim != 2
        or resource_amounts.ndim != 1
        or demand_expected.ndim != 1
        or costs.shape[0] != resource_amounts.shape[0]
        or costs.shape[1] != demand_expected.shape[0]
    ):
        raise ShapeMismatchError

    res = costs @ demand_expected
    return bool(np.all(res <= resource_amounts))
