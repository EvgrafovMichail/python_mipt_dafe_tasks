import numpy as np


class ShapeMismatchError(Exception):
    pass


def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:
    if costs.shape[0] == resource_amounts.shape[0] and costs.shape[1] == demand_expected.shape[0]:
        resource_required = costs @ demand_expected[..., np.newaxis]
        return np.all(resource_required.transpose() <= resource_amounts[np.newaxis, ...])
    raise ShapeMismatchError
