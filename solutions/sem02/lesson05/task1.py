import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape[0] != resource_amounts.shape[0] or demand_expected.shape[0] != costs.shape[1]:
        raise ShapeMismatchError()

    requiered_resources = demand_expected @ costs.T
    mask = requiered_resources <= resource_amounts
    res = resource_amounts[mask]

    if res.shape[0] == resource_amounts.shape[0]:
        return True
    return False
