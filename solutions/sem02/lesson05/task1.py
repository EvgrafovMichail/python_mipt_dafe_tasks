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


# costs = np.array([
#     [10,11,5],
#     [12,23,7],
#     [21,6,14],
#     [7,9,17],
#     [8,13,4]
# ])
# resource_amounts = np.array([500,92,400,25,118])
# demand_expected = np.array([8,9,6])

# print(can_satisfy_demand(costs,resource_amounts,demand_expected))
