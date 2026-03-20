import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape[0] != resource_amounts.shape[0] or costs.shape[1] != demand_expected.shape[0]:
        raise ShapeMismatchError

    costs_demand_expected = np.multiply(costs, demand_expected)
    resource_demand_expected = costs_demand_expected.sum(axis=1)
    answer = resource_demand_expected <= resource_amounts

    return np.all(answer)
