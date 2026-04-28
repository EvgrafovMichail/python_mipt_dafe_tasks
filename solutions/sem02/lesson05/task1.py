import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:

    n = costs.shape[1]
    m = costs.shape[0]
    if n != demand_expected.size or m != resource_amounts.size:
        raise ShapeMismatchError

    demand_expected = demand_expected[np.newaxis, :]
    costs *= demand_expected
    costs = np.sum(costs, axis=1, dtype=np.int64)

    resource_amounts -= costs
    resource_amounts = resource_amounts < 0

    return np.sum(resource_amounts) == 0
