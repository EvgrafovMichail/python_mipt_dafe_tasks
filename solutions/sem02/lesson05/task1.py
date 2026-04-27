import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    M, N = costs.shape

    if costs.ndim != 2 or len(resource_amounts) != M or len(demand_expected) != N:
        raise ShapeMismatchError

    resources_needed = costs @ demand_expected

    if np.any(resources_needed > resource_amounts):
        return False

    return True
