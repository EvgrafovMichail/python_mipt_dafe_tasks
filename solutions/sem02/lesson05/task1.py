import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    rows_count, column_count = costs.shape
    if rows_count != resource_amounts.shape[0] or column_count != demand_expected.shape[0]:
        raise ShapeMismatchError
    return np.all(costs @ demand_expected <= resource_amounts)
