import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    M, N = costs.shape
    if M != len(resource_amounts) or N != len(demand_expected):
        raise ShapeMismatchError

    resurce_need = costs @ demand_expected
    result = np.all(resurce_need <= resource_amounts)
    return result
