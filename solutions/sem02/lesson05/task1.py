import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape[0] != len(resource_amounts):
        raise ShapeMismatchError()
    if costs.shape[1] != len(demand_expected):
        raise ShapeMismatchError()

    matrix = costs @ demand_expected
    answer = (matrix <= resource_amounts).all()

    return answer
