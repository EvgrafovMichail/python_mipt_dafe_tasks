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

    costs_all_products = costs * demand_expected[np.newaxis, ...]
    return np.all(np.sum(costs_all_products, axis=1) <= resource_amounts)
