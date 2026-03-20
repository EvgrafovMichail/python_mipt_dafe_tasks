import numpy as np


class ShapeMismatchError(Exception):
    pass


# costs i,j - сколько едениц i ресурса требуется для j товара
#
#


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape != (resource_amounts.size, demand_expected.size):
        raise ShapeMismatchError

    resources_expected = costs @ demand_expected

    return np.sum(resources_expected > resource_amounts) == 0
