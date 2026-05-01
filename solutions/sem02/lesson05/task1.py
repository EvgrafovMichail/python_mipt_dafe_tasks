import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(costs: np.ndarray,resource_amounts: np.ndarray,demand_expected: np.ndarray,) -> bool:
    if costs.shape[0] != len(resource_amounts) or costs.shape[1] != len(demand_expected):
        raise ShapeMismatchError
    
    required_resources = costs @ demand_expected
    for i in range(len(required_resources)):
        if required_resources[i] > resource_amounts[i]:
            return False
    return True
    