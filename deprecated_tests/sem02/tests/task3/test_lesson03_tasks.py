import numpy as np
import pytest

from solutions.sem02.lesson03.task1 import ShapeMismatchError as Task1ShapeMismatchError
from solutions.sem02.lesson03.task1 import (
    compute_poly_vectorized,
    get_mutual_l2_distances_vectorized,
    sum_arrays_vectorized,
)
from solutions.sem02.lesson03.task2 import ShapeMismatchError as Task2ShapeMismatchError
from solutions.sem02.lesson03.task2 import convert_from_sphere, convert_to_sphere
from solutions.sem02.lesson03.task3 import get_extremum_indices


class TestTask1:
    @pytest.mark.parametrize(
        "lhs, rhs, result",
        [
            pytest.param([], [], [], id="empty"),
            pytest.param([1], [2], [3], id="one-elem"),
            pytest.param(
                [10, 20, 30, 40, 50], [1, 2, 3, 4, 5], [11, 22, 33, 44, 55], id="five-elem"
            ),
        ],
    )
    def test_sum_arrays(self, lhs: list, rhs: list, result: list):
        assert np.all(
            np.isclose(sum_arrays_vectorized(np.array(lhs), np.array(rhs)), np.array(result))
        )

    @pytest.mark.parametrize(
        "lhs, rhs",
        [
            pytest.param([], [1], id="first-empty"),
            pytest.param([1], [], id="second-empty"),
            pytest.param([1, 2], [1], id="first-longer"),
            pytest.param([1], [1, 2], id="second-longer"),
        ],
    )
    def test_sum_arrays_validate(self, lhs: list, rhs: list):
        with pytest.raises(Task1ShapeMismatchError):
            sum_arrays_vectorized(np.array(lhs), np.array(rhs))

    @pytest.mark.parametrize(
        "abscissa, result",
        [
            pytest.param([], [], id="empty"),
            pytest.param([1], [6], id="one-elem"),
            pytest.param([1, 2, 3, 4, 5], [6, 17, 34, 57, 86], id="five-elem"),
        ],
    )
    def test_compute_poly(self, abscissa: list, result: list):
        assert np.all(np.isclose(compute_poly_vectorized(np.array(abscissa)), np.array(result)))

    @staticmethod
    def get_mutual_l2_distances_naive(
        lhs: list[list[float]],
        rhs: list[list[float]],
    ) -> list[list[float]]:
        if len(lhs[0]) != len(rhs[0]):
            raise Task1ShapeMismatchError

        return [
            [
                sum((lhs[i][k] - rhs[j][k]) ** 2 for k in range(len(lhs[0]))) ** 0.5
                for j in range(len(rhs))
            ]
            for i in range(len(lhs))
        ]

    @pytest.mark.parametrize(
        "lhs, rhs",
        [
            pytest.param([[]], [[]], id="empty"),
            pytest.param([[1, 2, 3]], [[10, 20, 30]], id="one-vector"),
            pytest.param(
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                    [17, 18, 19, 20],
                ],
                [
                    [21, 22, 23, 24],
                    [25, 26, 27, 28],
                    [29, 30, 31, 32],
                    [33, 34, 35, 36],
                    [37, 38, 39, 40],
                ],
                id="five-vectors",
            ),
        ],
    )
    def test_get_mutual_l2_distances(self, lhs: list, rhs: list):
        assert np.all(
            np.isclose(
                get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs)),
                self.get_mutual_l2_distances_naive(lhs, rhs),
            )
        )

    @pytest.mark.parametrize(
        "lhs, rhs",
        [
            pytest.param([[]], [[1]], id="first-empty"),
            pytest.param([[1]], [[]], id="second-empty"),
            pytest.param([[1, 2], [3, 4]], [[1], [2]], id="first-longer"),
            pytest.param([[1], [2]], [[1, 2], [3, 4]], id="second-longer"),
        ],
    )
    def test_get_mutual_l2_distances_validate(self, lhs: list, rhs: list):
        with pytest.raises(Task1ShapeMismatchError):
            sum_arrays_vectorized(np.array(lhs), np.array(rhs))


class TestTask2:
    @pytest.mark.parametrize(
        "distances, azimuth, inclination, expected_x, expected_y, expected_z",
        [
            pytest.param(
                np.array([1.0]),
                np.array([0.0]),
                np.array([np.pi / 2]),
                np.array([1.0]),
                np.array([0.0]),
                np.array([0.0]),
                id="on_positive_x_axis",
            ),
            pytest.param(
                np.array([2.0]),
                np.array([np.pi / 2]),
                np.array([np.pi / 2]),
                np.array([0.0]),
                np.array([2.0]),
                np.array([0.0]),
                id="on_positive_y_axis",
            ),
            pytest.param(
                np.array([3.0]),
                np.array([0.0]),
                np.array([0.0]),
                np.array([0.0]),
                np.array([0.0]),
                np.array([3.0]),
                id="on_positive_z_axis",
            ),
            pytest.param(
                np.array([5.0]),
                np.array([np.pi]),
                np.array([np.pi / 2]),
                np.array([-5.0]),
                np.array([0.0]),
                np.array([0.0]),
                id="on_negative_x_axis",
            ),
        ],
    )
    def test_convert_from_sphere(
        self, distances, azimuth, inclination, expected_x, expected_y, expected_z
    ):
        x, y, z = convert_from_sphere(distances, azimuth, inclination)
        assert np.allclose(x, expected_x)
        assert np.allclose(y, expected_y)
        assert np.allclose(z, expected_z)

    @pytest.mark.parametrize(
        "expected_distances, expected_azimuth, expected_inclination, x, y, z",
        [
            pytest.param(
                np.array([1.0]),
                np.array([0.0]),
                np.array([np.pi / 2]),
                np.array([1.0]),
                np.array([0.0]),
                np.array([0.0]),
                id="on-positive-x-axis",
            ),
            pytest.param(
                np.array([2.0]),
                np.array([np.pi / 2]),
                np.array([np.pi / 2]),
                np.array([0.0]),
                np.array([2.0]),
                np.array([0.0]),
                id="on-positive-y-axis",
            ),
            pytest.param(
                np.array([3.0]),
                np.array([0.0]),
                np.array([0.0]),
                np.array([0.0]),
                np.array([0.0]),
                np.array([3.0]),
                id="on-positive-z-axis",
            ),
            pytest.param(
                np.array([5.0]),
                np.array([np.pi]),
                np.array([np.pi / 2]),
                np.array([-5.0]),
                np.array([0.0]),
                np.array([0.0]),
                id="on-negative-x-axis",
            ),
        ],
    )
    def test_convert_to_sphere(
        self, expected_distances, expected_azimuth, expected_inclination, x, y, z
    ):
        distances, azimuth, inclination = convert_to_sphere(x, y, z)
        assert np.allclose(distances, expected_distances)
        assert np.allclose(azimuth, expected_azimuth)
        assert np.allclose(inclination, expected_inclination)

    @pytest.mark.parametrize(
        "dist, az, inc",
        [
            pytest.param(np.array([1, 2]), np.array([0]), np.array([0]), id="dist-longer"),
            pytest.param(np.array([1]), np.array([0, 1]), np.array([0]), id="azimuth-longer"),
            pytest.param(np.array([1]), np.array([0]), np.array([0, 1]), id="inclination-longer"),
            pytest.param(
                np.array([[1, 2], [2, 3], [2, 3]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                id="dist-shape-mis-2d",
            ),
            pytest.param(
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2], [2, 3], [2, 3]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                id="azimuth-shape-mis-2d",
            ),
            pytest.param(
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2], [2, 3], [2, 3]]),
                id="inclination-shape-mis-2d",
            ),
        ],
    )
    def test_shape_mismatch_from_sphere(self, dist, az, inc):
        with pytest.raises(Task2ShapeMismatchError):
            convert_from_sphere(dist, az, inc)

    @pytest.mark.parametrize(
        "x, y, z",
        [
            pytest.param(np.array([1, 2]), np.array([0]), np.array([0]), id="x-longer"),
            pytest.param(np.array([1]), np.array([0, 1]), np.array([0]), id="y-longer"),
            pytest.param(np.array([1]), np.array([0]), np.array([0, 1]), id="z-longer"),
            pytest.param(
                np.array([[1, 2], [2, 3], [2, 3]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                id="x-shape-mis-2d",
            ),
            pytest.param(
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2], [2, 3], [2, 3]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                id="y-shape-mis-2d",
            ),
            pytest.param(
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2, 3], [2, 3, 4]]),
                np.array([[1, 2], [2, 3], [2, 3]]),
                id="z-shape-mis-2d",
            ),
        ],
    )
    def test_shape_mismatch_to_sphere(self, x, y, z):
        with pytest.raises(Task2ShapeMismatchError):
            convert_to_sphere(x, y, z)

    def test_convert_from_sphere_2d(self):
        distances = np.array(
            [
                [1.0, 2.0, 3.0, 4.0, 5.0],
                [2.5, 3.5, 1.5, 4.5, 0.5],
                [1.0, 1.0, 2.0, 2.0, 3.0],
                [3.0, 2.0, 1.0, 2.0, 1.0],
                [5.0, 4.0, 3.0, 2.0, 1.0],
            ]
        )

        azimuth = np.array(
            [
                [0.0, np.pi / 2, np.pi, -np.pi / 2, np.pi / 4],
                [np.pi / 3, -np.pi / 3, 0.0, np.pi / 6, -np.pi / 6],
                [np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2],
                [0.0, 0.0, 0.0, 0.0, 0.0],
                [-np.pi / 4, np.pi / 3, -np.pi / 3, np.pi / 6, -np.pi / 6],
            ]
        )

        inclination = np.array(
            [
                [np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2],
                [np.pi / 3, np.pi / 4, np.pi / 6, np.pi / 3, np.pi / 4],
                [0.0, np.pi / 2, np.pi, np.pi / 3, 2 * np.pi / 3],
                [np.pi / 4, np.pi / 3, np.pi / 2, 2 * np.pi / 3, np.pi],
                [np.pi / 6, np.pi / 3, np.pi / 2, 2 * np.pi / 3, 5 * np.pi / 6],
            ]
        )

        expected_x = np.array(
            [
                [1.00000000e00, 1.22464680e-16, -3.00000000e00, 2.44929360e-16, 3.53553391e00],
                [1.08253175e00, 1.23743687e00, 7.50000000e-01, 3.37500000e00, 3.06186218e-01],
                [0.00000000e00, 6.12323400e-17, 1.49975978e-32, 1.06057524e-16, 1.59086286e-16],
                [2.12132034e00, 1.73205081e00, 1.00000000e00, 1.73205081e00, 1.22464680e-16],
                [1.76776695e00, 1.73205081e00, 1.50000000e00, 1.50000000e00, 4.33012702e-01],
            ]
        )

        expected_y = np.array(
            [
                [0.00000000e00, 2.00000000e00, 3.67394040e-16, -4.00000000e00, 3.53553391e00],
                [1.87500000e00, -2.14330352e00, 0.00000000e00, 1.94855716e00, -1.76776695e-01],
                [0.00000000e00, 1.00000000e00, 2.44929360e-16, 1.73205081e00, 2.59807621e00],
                [0.00000000e00, 0.00000000e00, 0.00000000e00, 0.00000000e00, 0.00000000e00],
                [-1.76776695e00, 3.00000000e00, -2.59807621e00, 8.66025404e-01, -2.50000000e-01],
            ]
        )

        expected_z = np.array(
            [
                [6.12323400e-17, 1.22464680e-16, 1.83697020e-16, 2.44929360e-16, 3.06161700e-16],
                [1.25000000e00, 2.47487373e00, 1.29903811e00, 2.25000000e00, 3.53553391e-01],
                [1.00000000e00, 6.12323400e-17, -2.00000000e00, 1.00000000e00, -1.50000000e00],
                [2.12132034e00, 1.00000000e00, 6.12323400e-17, -1.00000000e00, -1.00000000e00],
                [4.33012702e00, 2.00000000e00, 1.83697020e-16, -1.00000000e00, -8.66025404e-01],
            ]
        )

        x, y, z = convert_from_sphere(distances, azimuth, inclination)

        assert x.shape == (5, 5)
        assert y.shape == (5, 5)
        assert z.shape == (5, 5)

        assert np.allclose(x, expected_x, atol=1e-6)
        assert np.allclose(y, expected_y, atol=1e-6)
        assert np.allclose(z, expected_z, atol=1e-6)

    def test_convert_to_sphere_2d(self):
        x = np.array(
            [
                [1.0, 0.0, -1.0, 0.0, 1.0],
                [0.0, 2.0, 0.0, -2.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0],
                [3.0, -3.0, 3.0, -3.0, 0.0],
                [1.0, -1.0, 1.0, -1.0, 2.0],
            ]
        )

        y = np.array(
            [
                [0.0, 1.0, 0.0, -1.0, 1.0],
                [2.0, 0.0, -2.0, 0.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 4.0],
                [1.0, 1.0, -1.0, -1.0, 0.0],
            ]
        )

        z = np.array(
            [
                [0.0, 0.0, 0.0, 0.0, np.sqrt(2)],
                [0.0, 0.0, 0.0, 0.0, np.sqrt(2)],
                [0.0, 1.0, -1.0, 2.0, -2.0],
                [0.0, 0.0, 3.0, -3.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0],
            ]
        )

        expected_distances = np.array(
            [
                [1.0, 1.0, 1.0, 1.0, 2.0],
                [2.0, 2.0, 2.0, 2.0, 2.0],
                [0.0, 1.0, 1.0, 2.0, 2.0],
                [3.0, 3.0, 4.24264069, 4.24264069, 4.0],
                [1.41421356, 1.41421356, 1.41421356, 1.41421356, 2.0],
            ]
        )

        expected_azimuth = np.array(
            [
                [0.0, 1.57079633, 3.14159265, -1.57079633, 0.78539816],
                [1.57079633, 0.0, -1.57079633, 3.14159265, 0.78539816],
                [0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 3.14159265, 0.0, 3.14159265, 1.57079633],
                [0.78539816, 2.35619449, -0.78539816, -2.35619449, 0.0],
            ]
        )

        expected_inclination = np.array(
            [
                [1.57079633, 1.57079633, 1.57079633, 1.57079633, 0.78539816],
                [1.57079633, 1.57079633, 1.57079633, 1.57079633, 0.78539816],
                [0.0, 0.0, 3.14159265, 0.0, 3.14159265],
                [1.57079633, 1.57079633, 0.78539816, 2.35619449, 1.57079633],
                [1.57079633, 1.57079633, 1.57079633, 1.57079633, 1.57079633],
            ]
        )

        distances, azimuth, inclination = convert_to_sphere(x, y, z)

        assert distances.shape == (5, 5)
        assert azimuth.shape == (5, 5)
        assert inclination.shape == (5, 5)

        assert np.allclose(distances, expected_distances, atol=1e-6)
        assert np.allclose(azimuth, expected_azimuth, atol=1e-6)
        assert np.allclose(inclination, expected_inclination, atol=1e-6)


class TestTask3:
    @pytest.mark.parametrize(
        "ordinates, expected_mins, expected_maxs",
        [
            pytest.param(
                np.array([1.0, 3.0, 2.0]),
                np.array([], dtype=int),
                np.array([1]),
                id="single_maximum",
            ),
            pytest.param(
                np.array([3.0, 1.0, 2.0]),
                np.array([1]),
                np.array([], dtype=int),
                id="single_minimum",
            ),
            pytest.param(
                np.array([1.0, 3.0, 1.0, 4.0, 2.0]),
                np.array([2]),
                np.array([1, 3]),
                id="min_and_max",
            ),
            pytest.param(
                np.array([1.0, 2.0, 2.0, 1.0]),
                np.array([], dtype=int),
                np.array([], dtype=int),
                id="plateau_no_extremum",
            ),
            pytest.param(
                np.array([1.0, 0.0, 0.0, 1.0]),
                np.array([], dtype=int),
                np.array([], dtype=int),
                id="plateau_no_extremum2",
            ),
            pytest.param(
                np.array([1.0, 2.0, 3.0, 4.0]),
                np.array([], dtype=int),
                np.array([], dtype=int),
                id="strictly_increasing",
            ),
            pytest.param(
                np.array([4.0, 3.0, 2.0, 1.0]),
                np.array([], dtype=int),
                np.array([], dtype=int),
                id="strictly_decreasing",
            ),
            pytest.param(
                np.array([0.0, 1.0, 0.0, 2.0, 0.0, 3.0, 0.0]),
                np.array([2, 4]),
                np.array([1, 3, 5]),
                id="alternating_extrema",
            ),
            pytest.param(
                np.array([5.0, 5.0, 5.0, 5.0]),
                np.array([], dtype=int),
                np.array([], dtype=int),
                id="constant_array",
            ),
            pytest.param(
                np.array([5.0, 3.0, 3.0, 3.0, 0.0]),
                np.array([], dtype=int),
                np.array([], dtype=int),
                id="edges_ignored",
            ),
        ],
    )
    def test_get_extremum_indices(self, ordinates, expected_mins, expected_maxs):
        mins, maxs = get_extremum_indices(ordinates)

        assert np.array_equal(mins, expected_mins), f"Expected mins {expected_mins}, got {mins}"
        assert np.array_equal(maxs, expected_maxs), f"Expected maxs {expected_maxs}, got {maxs}"

    def test_get_extremum_indices_validation(self):
        with pytest.raises(ValueError):
            get_extremum_indices(np.array([1.0]))

        with pytest.raises(ValueError):
            get_extremum_indices(np.array([1.0, 2.0]))
