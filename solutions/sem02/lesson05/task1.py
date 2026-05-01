import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if len(costs) != len(resource_amounts):
        raise ShapeMismatchError

    if costs.shape[1] != len(demand_expected):
        raise ShapeMismatchError

    lacking_resources = resource_amounts.reshape(-1) < costs @ demand_expected

    return not np.sum(lacking_resources)
