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

    required = costs @ demand_expected
    ans = required <= resource_amounts
    ans = ans.all()
    return ans
