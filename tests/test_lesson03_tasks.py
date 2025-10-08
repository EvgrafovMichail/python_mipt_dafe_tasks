import pytest

from solutions.lesson03.task1 import flip_bits_in_range
from solutions.lesson03.task2 import get_cube_root
from solutions.lesson03.task3 import get_nth_digit


@pytest.mark.parametrize(
    "num, left_bit, right_bit, result_expected",
    [
        pytest.param(0b1011, 1, 1, 0b1010, id="invert_lsb"),
        pytest.param(0b1011, 2, 2, 0b1001, id="invert_second_bit"),
        pytest.param(0b1000, 1, 3, 0b1111, id="invert_bits_1_to_3"),
        pytest.param(0b1011, 1, 4, 0b0100, id="invert_all_4_bits"),
        pytest.param(0, 1, 5, 0b11111, id="invert_zero_range"),
        pytest.param(0b11111, 2, 4, 0b10001, id="invert_middle_bits"),
        pytest.param(0b1000000, 7, 7, 0b0000000, id="invert_single_high_bit"),
        pytest.param(0b10101010, 1, 8, 0b01010101, id="invert_full_byte"),
        pytest.param(0b11111, 1, 5, 0, id="invert_to_zero"),
    ],
)
def test_flip_bits_in_range(num: int, left_bit: int, right_bit: int, result_expected: int):
    assert flip_bits_in_range(num, left_bit, right_bit) == result_expected


@pytest.mark.parametrize(
    "n, eps",
    [
        pytest.param(27, 1e-6, id="positive_perfect_cube"),
        pytest.param(-8, 1e-6, id="negative_perfect_cube"),
        pytest.param(0.125, 1e-3, id="fractional_positive"),
        pytest.param(-0.001, 1e-3, id="fractional_negative"),
        pytest.param(0, 1e-5, id="zero"),
        pytest.param(2, 1e-7, id="irrational_root"),
        pytest.param(-27, 1e-1, id="negative_large_cube"),
        pytest.param(1, 1e-4, id="one"),
        pytest.param(-1, 1e-4, id="minus_one"),
        pytest.param(0.000001, 1e-1, id="very_small_positive"),
        pytest.param(1_000_000_000, 1e-5, id="large_positive_number"),
    ],
)
def test_get_cube_root(n: float, eps: float):
    result = get_cube_root(n, eps)
    assert abs(result**3 - n) < eps


@pytest.mark.parametrize(
    "n, result_expected",
    [
        pytest.param(1, 0, id="one"),
        pytest.param(5, 8, id="five"),
        pytest.param(10, 1, id="ten"),
        pytest.param(100, 0, id="hundred"),
        pytest.param(1001, 2, id="thousand_one"),
        pytest.param(10**8, 3, id="hundred_million"),
        pytest.param(10**9, 6, id="billion"),
    ],
)
def test_get_nth_digit(n: int, result_expected: int):
    assert get_nth_digit(n) == result_expected
