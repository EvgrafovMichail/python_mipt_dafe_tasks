import os

import numpy as np
import pytest

from solutions.sem02.lesson05.task1 import ShapeMismatchError as Task1ShapeMismatchError
from solutions.sem02.lesson05.task1 import can_satisfy_demand
from solutions.sem02.lesson05.task2 import ShapeMismatchError as Task2ShapeMismatchError
from solutions.sem02.lesson05.task2 import get_projections_components
from solutions.sem02.lesson05.task3 import ShapeMismatchError as Task3ShapeMismatchError
from solutions.sem02.lesson05.task3 import adaptive_filter

DATA_PATH = os.path.join("tests", "test_data", "lesson05")


class TestTask1:
    @pytest.mark.parametrize(
        "costs, resource_amounts, demand_expected, expected",
        [
            pytest.param(
                np.eye(2),
                np.array([3.0, 3.0]),
                np.array([2, 2]),
                True,
                id="identity_enough",
            ),
            pytest.param(
                np.eye(2),
                np.array([2.0, 2.0]),
                np.array([3, 3]),
                False,
                id="identity_not_enough",
            ),
            pytest.param(
                np.array([[1.0, 2.0], [3.0, 4.0]]),
                np.array([10.0, 20.0]),
                np.array([2, 3]),
                True,
                id="general_enough",
            ),
            pytest.param(
                np.array([[1.0, 2.0], [3.0, 4.0]]),
                np.array([7.0, 17.0]),
                np.array([2, 3]),
                False,
                id="general_not_enough",
            ),
            pytest.param(
                np.array([[1.0]]),
                np.array([5.0]),
                np.array([5]),
                True,
                id="single_resource_product_exact",
            ),
            pytest.param(
                np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]]),
                np.array([3.0, 3.0]),
                np.array([1, 1, 1]),
                True,
                id="non_square_costs_enough",
            ),
            pytest.param(
                np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]]),
                np.array([1.0, 1.0]),
                np.array([1, 1, 1]),
                False,
                id="non_square_costs_not_enough",
            ),
            pytest.param(
                np.eye(3),
                np.array([0.0, 0.0, 0.0]),
                np.array([0, 0, 0]),
                True,
                id="zero_demand",
            ),
            pytest.param(
                np.eye(2),
                np.full(shape=2, fill_value=3),
                np.full(shape=2, fill_value=2),
                True,
                id="notebook_satisfy",
            ),
            pytest.param(
                np.eye(2),
                np.full(shape=2, fill_value=2),
                np.full(shape=2, fill_value=3),
                False,
                id="notebook_not_satisfy",
            ),
        ],
    )
    def test_can_satisfy_demand(self, costs, resource_amounts, demand_expected, expected):
        assert can_satisfy_demand(costs, resource_amounts, demand_expected) == expected

    def test_can_satisfy_demand_validate(self):
        with pytest.raises(Task1ShapeMismatchError):
            can_satisfy_demand(
                np.array([[1.0, 2.0, 3.0]]),
                np.array([1.0, 2.0]),
                np.array([1]),
            )

        with pytest.raises(Task1ShapeMismatchError):
            can_satisfy_demand(
                np.array([[1.0, 2.0]]),
                np.array([1.0]),
                np.array([1, 2, 3]),
            )


class TestTask2:
    @pytest.mark.parametrize(
        "matrix, vector, proj_expected, orth_expected",
        [
            pytest.param(
                np.diag([2.0, 3.0]),
                np.array([1.0, 2.0]),
                np.array([[1.0, 0.0], [0.0, 2.0]]),
                np.array([[0.0, 2.0], [1.0, 0.0]]),
                id="diagonal_basis",
            ),
            pytest.param(
                np.array([[1.0, 0.0], [1.0, 1.0]]),
                np.array([0.0, 1.0]),
                np.array([[0.0, 0.0], [0.5, 0.5]]),
                np.array([[0.0, 1.0], [-0.5, 0.5]]),
                id="non_orthogonal_basis",
            ),
            pytest.param(
                np.eye(3),
                np.array([1.0, 2.0, 3.0]),
                np.array([[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]),
                np.array([[0.0, 2.0, 3.0], [1.0, 0.0, 3.0], [1.0, 2.0, 0.0]]),
                id="identity_3d",
            ),
            pytest.param(
                np.array([[1.0, 2.0], [2.0, 4.0]]),
                np.array([0.0, 1.0]),
                None,
                None,
                id="singular_not_basis",
            ),
            pytest.param(
                np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]),
                np.array([1.0, 2.0, 3.0]),
                None,
                None,
                id="rank_deficient_3d",
            ),
            pytest.param(
                np.diag([2, 3]),
                np.arange(start=1, stop=3),
                np.array([[1, 0], [0, 2]]),
                np.array([[0, 2], [1, 0]]),
                id="notebook_diagonal",
            ),
            pytest.param(
                np.array([[1, 0], [1, 1]]),
                np.array([0, 1]),
                np.array([[0, 0], [0.5, 0.5]]),
                np.array([[0, 1], [-0.5, 0.5]]),
                id="notebook_non_orthogonal",
            ),
            pytest.param(
                np.array([[1, 2], [2, 4]]),
                np.array([0, 1]),
                None,
                None,
                id="notebook_singular",
            ),
        ],
    )
    def test_get_projections_components(self, matrix, vector, proj_expected, orth_expected):
        projections, orthogonals = get_projections_components(matrix, vector)

        if proj_expected is None:
            assert projections is None
            assert orthogonals is None
        else:
            assert np.allclose(projections, proj_expected)
            assert np.allclose(orthogonals, orth_expected)

    def test_get_projections_components_validate(self):
        with pytest.raises(Task2ShapeMismatchError):
            get_projections_components(
                np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                np.array([1.0, 2.0, 3.0]),
            )

        with pytest.raises(Task2ShapeMismatchError):
            get_projections_components(
                np.array([[1.0, 0.0], [0.0, 1.0]]),
                np.array([1.0, 2.0, 3.0]),
            )


class TestTask3:
    def test_adaptive_filter(self):
        diag_A = np.load(os.path.join(DATA_PATH, "diag_A_data.npy"))
        Vj = np.load(os.path.join(DATA_PATH, "Vj_data.npy"))
        Vs = np.load(os.path.join(DATA_PATH, "Vs_data.npy"))
        y_expected = np.load(os.path.join(DATA_PATH, "y_data.npy"))

        y = adaptive_filter(Vs, Vj, diag_A)

        assert y.shape == y_expected.shape
        assert np.allclose(y, y_expected)

    def test_adaptive_filter_validate(self):
        with pytest.raises(Task3ShapeMismatchError):
            adaptive_filter(
                np.array([[1.0], [2.0]]),
                np.array([[1.0], [2.0], [3.0]]),
                np.array([1.0]),
            )

        with pytest.raises(Task3ShapeMismatchError):
            adaptive_filter(
                np.array([[1.0], [2.0]]),
                np.array([[1.0, 2.0], [3.0, 4.0]]),
                np.array([1.0, 2.0, 3.0]),
            )
