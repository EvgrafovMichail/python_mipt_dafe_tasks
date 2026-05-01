import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    m, n = costs.shape
    if (
        resource_amounts.ndim != 1
        or demand_expected.ndim != 1
        or resource_amounts.shape[0] != m
        or demand_expected.shape[0] != n
    ):
        raise ShapeMismatchError

    resource_needs = costs @ demand_expected

    return (resource_amounts >= resource_needs).all()
