import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape[0] != resource_amounts.size or costs.shape[1] != demand_expected.size:
        raise ShapeMismatchError

    amount_resources_needed = np.sum(costs * demand_expected, axis=1)
    return all(amount_resources_needed <= resource_amounts)
