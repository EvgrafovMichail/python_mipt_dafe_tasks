import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if np.shape(costs) != (len(resource_amounts), len(demand_expected)):
        raise ShapeMismatchError

    needs = costs @ demand_expected

    mask = needs > resource_amounts
    if np.any(mask):
        return False

    return True
