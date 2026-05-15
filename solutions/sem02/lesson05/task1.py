import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:

    M, N = costs.shape

    if resource_amounts.size != M or demand_expected.size != N:
        raise ShapeMismatchError

    need_resurses = costs @ demand_expected
    check_mask = need_resurses <= resource_amounts

    return np.all(check_mask)
