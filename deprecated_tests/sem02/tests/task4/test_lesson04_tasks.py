import os

import numpy as np
import pytest

from solutions.sem02.lesson04.task1 import blur_image, pad_image
from solutions.sem02.lesson04.task2 import get_dominant_color_info

DATA_PATH = os.path.join("test_data", "lesson04")


class TestTask1:
    @pytest.mark.parametrize(
        "image, pad_size, expected",
        [
            pytest.param(
                np.array([[5]], dtype=np.float32),
                1,
                np.array(
                    [
                        [0, 0, 0],
                        [0, 5, 0],
                        [0, 0, 0],
                    ],
                    dtype=np.float32,
                ),
                id="2d_single_pixel_pad_1",
            ),
            pytest.param(
                np.array([[5]], dtype=np.float32),
                2,
                np.array(
                    [
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 5, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                    ],
                    dtype=np.float32,
                ),
                id="2d_single_pixel_pad_2",
            ),
            pytest.param(
                np.array([[1, 2], [3, 4]], dtype=np.uint8),
                1,
                np.array(
                    [[0, 0, 0, 0], [0, 1, 2, 0], [0, 3, 4, 0], [0, 0, 0, 0]],
                    dtype=np.uint8,
                ),
                id="2d_pad_1",
            ),
            pytest.param(
                np.array([[1, 2], [3, 4]], dtype=np.uint8),
                2,
                np.array(
                    [
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 2, 0, 0],
                        [0, 0, 3, 4, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                    ],
                    dtype=np.uint8,
                ),
                id="2d_pad_2",
            ),
            pytest.param(
                np.array([[1, 2]], dtype=np.uint8),
                2,
                np.array(
                    [
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 2, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                    ],
                    dtype=np.uint8,
                ),
                id="2d_row_pad_2",
            ),
            pytest.param(
                np.array([[1], [2]], dtype=np.uint8),
                2,
                np.array(
                    [
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 2, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                    ],
                    dtype=np.uint8,
                ),
                id="2d_col_pad_2",
            ),
            pytest.param(
                np.array([[[10, 20, 30], [40, 50, 60]]], dtype=np.uint8),
                1,
                np.array(
                    [
                        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                        [[0, 0, 0], [10, 20, 30], [40, 50, 60], [0, 0, 0]],
                        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    ],
                    dtype=np.uint8,
                ),
                id="3d_rgb_pad_1",
            ),
            pytest.param(
                np.array([[[10, 20, 30], [40, 50, 60]]], dtype=np.uint8),
                2,
                np.array(
                    [
                        [
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                        ],
                        [
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                        ],
                        [
                            [0, 0, 0],
                            [0, 0, 0],
                            [10, 20, 30],
                            [40, 50, 60],
                            [0, 0, 0],
                            [0, 0, 0],
                        ],
                        [
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                        ],
                        [
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                        ],
                    ],
                    dtype=np.uint8,
                ),
                id="3d_rgb_pad_2",
            ),
            pytest.param(
                np.zeros((2, 3), dtype=int),
                1,
                np.zeros((4, 5), dtype=int),
                id="2d_zeros_pad_1",
            ),
            pytest.param(
                np.arange(4095 * 4095).reshape(4095, 4095) % 256,
                100,
                np.load(os.path.join(DATA_PATH, "test_task11_data_res.npy")),
                id="large_data",
            ),
        ],
    )
    def test_pad_image(self, image, pad_size, expected):
        result = pad_image(image.astype(np.uint8), pad_size)

        assert np.array_equal(result, expected)
        assert result.dtype == np.uint8

    def test_pad_size_validate(self):
        image = np.array([[1, 2], [3, 4]])

        with pytest.raises(ValueError):
            pad_image(image, 0)

        with pytest.raises(ValueError):
            pad_image(image, -1)

    @pytest.mark.parametrize(
        "image, kernel_size, expected",
        [
            pytest.param(
                np.array([[10, 20], [30, 40]], dtype=np.uint8),
                1,
                np.array([[10, 20], [30, 40]], dtype=np.uint8),
                id="kernel_size_1",
            ),
            pytest.param(
                np.array([[100, 100], [100, 100]], dtype=np.uint8),
                3,
                np.array([[44, 44], [44, 44]], dtype=np.uint8),
                id="2d_constant_blur_3",
            ),
            pytest.param(
                np.array([[0, 0, 0], [0, 255, 0], [0, 0, 0]], dtype=np.uint8),
                3,
                np.array([[28, 28, 28], [28, 28, 28], [28, 28, 28]], dtype=np.uint8),
                id="2d_single_pixel_blur_3",
            ),
            pytest.param(
                np.array([[100]], dtype=np.uint8),
                3,
                np.array([[11]], dtype=np.uint8),
                id="2d_1x1_blur_3",
            ),
            pytest.param(
                np.array(
                    [[[100, 68, 50], [179, 30, 245]], [[40, 90, 235], [38, 70, 210]]],
                    dtype=np.uint8,
                ),
                3,
                np.array(
                    [[[39, 28, 82], [39, 28, 82]], [[39, 28, 82], [39, 28, 82]]],
                    dtype=np.uint8,
                ),
                id="3d_blur_3",
            ),
            pytest.param(
                np.arange(4095 * 4095 * 2).reshape(4095, 4095 * 2) % 256,
                5,
                np.load(os.path.join(DATA_PATH, "test_task12_data_res.npy")),
                id="large_data",
            ),
        ],
    )
    def test_blur_image(self, image, kernel_size, expected):
        result = blur_image(image.astype(np.uint8), kernel_size)

        assert result.shape == expected.shape
        assert result.dtype == expected.dtype
        assert np.all(np.abs(result.astype(np.int16) - expected.astype(np.int16)) < 2)

    def test_blur_image_validate(self):
        image = np.array([[1, 2], [3, 4]], dtype=np.uint8)

        with pytest.raises(ValueError):
            blur_image(image, 2)
        with pytest.raises(ValueError):
            blur_image(image, 4)

        with pytest.raises(ValueError):
            blur_image(image, 0)
        with pytest.raises(ValueError):
            blur_image(image, -1)


class TestTask2:
    @pytest.mark.parametrize(
        "image, threshold, expected_color, expected_ratio",
        [
            pytest.param(
                np.array([[100, 100], [100, 100]], dtype=np.uint8),
                5,
                [100],
                1.0,
                id="uniform_image",
            ),
            pytest.param(
                np.array([[50, 52], [51, 100]], dtype=np.uint8),
                3,
                [50, 51, 52],
                0.75,
                id="close_colors_merged",
            ),
            pytest.param(
                np.array([[0, 0], [10, 11]], dtype=np.uint8),
                10,
                [0],
                0.5,
                id="distant_colors_not_merged",
            ),
            pytest.param(
                np.array([[21, 20, 10], [20, 30, 20]], dtype=np.uint8),
                1,
                [20],
                0.5,
                id="threshold_1_only_exact",
            ),
            pytest.param(
                np.array([[0, 100, 200]], dtype=np.uint8),
                10,
                [0, 100, 200],
                1 / 3,
                id="all_colors_different",
            ),
            pytest.param(
                np.array([[100, 100, 100, 102, 104, 106, 108]], dtype=np.uint8),
                3,
                [102],
                5 / 7,
                id="chain_within_threshold",
            ),
            pytest.param(
                np.array([[255, 0, 0]], dtype=np.uint8),
                20,
                [0],
                2 / 3,
                id="marginal_values_1",
            ),
            pytest.param(
                np.array([[0, 255, 0]], dtype=np.uint8),
                20,
                [0],
                2 / 3,
                id="marginal_values_2",
            ),
            pytest.param(
                np.array([[0, 0, 255]], dtype=np.uint8),
                20,
                [0],
                2 / 3,
                id="marginal_values_3",
            ),
            pytest.param(
                np.load(os.path.join(DATA_PATH, "test_task2_data1.npy")),
                10,
                list(range(100 - 11, 100 + 11)),
                0.166868359375,
                id="large_data",
            ),
        ],
    )
    def test_get_dominant_color_info(self, image, threshold, expected_color, expected_ratio):
        color, ratio_percent = get_dominant_color_info(image.astype(np.uint8), threshold)

        assert color in expected_color
        assert (abs(ratio_percent - expected_ratio * 100) < 1e-6) or (
            abs(ratio_percent - expected_ratio) < 1e-6
        )
        assert isinstance(color, np.uint8)

    def test_get_dominant_color_info_validate(self):
        image = np.array([[0, 255]], dtype=np.uint8)

        with pytest.raises(ValueError, match="threshold must be positive"):
            get_dominant_color_info(image, 0)

        with pytest.raises(ValueError, match="threshold must be positive"):
            get_dominant_color_info(image, -1)
