import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    M, N = costs.shape
    if resource_amounts.shape[0] != M or demand_expected.shape[0] != N:
        raise ShapeMismatchError

    zatraty = costs @ demand_expected
    return np.all(zatraty <= resource_amounts)
