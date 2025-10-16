import pytest 
import random

from solutions.lesson04.task1 import is_arithmetic_progression
from solutions.lesson04.task2 import merge_intervals
from solutions.lesson04.task3 import find_single_number
from solutions.lesson04.task4 import move_zeros_to_end
from solutions.lesson04.task5 import find_row_with_most_ones
from solutions.lesson04.task6 import count_cycles

@pytest.mark.parametrize("lst, expected", [
    pytest.param([], True, id="empty_list"),
    pytest.param([5], True, id="single_element"),
    pytest.param([1, 3], True, id="two_elements"),
    pytest.param([3, 1], True, id="two_elements_unsorted"),
    pytest.param([1, 3, 5, 7], True, id="already_sorted_ap"),
    pytest.param([3, 1, 5, 7], True, id="unsorted_ap"),
    pytest.param([1, 2, 4], False, id="not_ap"),
    pytest.param([10, 5, 0, -5], True, id="negative_difference"),
    pytest.param([1, 1, 1, 1], True, id="constant_sequence"),
    pytest.param([1, 2, 3, 5], False, id="almost_ap_but_not"),
    pytest.param([0, 0, 1], False, id="two_same_one_different"),
    pytest.param([10**5 + i*10**2 for i in range(1000)], True, id="long_list_true"),
    pytest.param([10**5 + i*10**2 for i in range(999)] + [1], False, id="long_list_false"),
])
def test_is_arithmetic_progression_parametrized(lst, expected):
    if len(lst) > 500:
        random.shuffle(lst)
    assert is_arithmetic_progression(lst) == expected


@pytest.mark.parametrize("intervals, expected", [
    pytest.param([], [], id="empty"),
    pytest.param([[1, 3]], [[1, 3]], id="single_interval"),
    pytest.param([[10, 13], [1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 13], [15, 18]], id="classic_merge"),
    pytest.param([[1, 4], [4, 5]], [[1, 5]], id="touching_intervals"),
    pytest.param([[1, 4], [2, 3]], [[1, 4]], id="nested_interval"),
    pytest.param([[5, 7], [1, 3], [15, 20], [0, 0], [2, 4], [6, 10], [0, 2]], [[0, 4], [5, 10], [15, 20]], id="unsorted_input"),
    pytest.param([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]], id="no_overlap"),
    pytest.param([[1, 10], [2, 3], [4, 5], [6, 7]], [[1, 10]], id="all_merged"),
])
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected

@pytest.mark.parametrize("nums, expected", [
    pytest.param([2, 2, 1], 1, id="simple_case"),
    pytest.param([4, 1, 2, 1, 2], 4, id="middle_single"),
    pytest.param([1], 1, id="single_element"),
    pytest.param([100, 200, 300, 200, 100], 300, id="large_numbers"),
    pytest.param([0, 1, 0], 1, id="with_zero"),
    pytest.param([7, 8, 9, 8, 7], 9, id="unsorted"),
    pytest.param([i + 10**5 for i in range(500)] + [i + 10**5 for i in range(500)] + [69], 69, id="long_list"),
])
def test_find_single_number(nums, expected):
    assert find_single_number(nums) == expected

@pytest.mark.parametrize("input_list, expected_list, expected_index", [
    pytest.param([0, 1, 0, 3, 12], [1, 3, 12, 0, 0], 3, id="basic"),
    pytest.param([0, 0, 1], [1, 0, 0], 1, id="zeros_first"),
    pytest.param([1, 2, 3], [1, 2, 3], 3, id="no_zeros"),
    pytest.param([0, 0, 0], [0, 0, 0], 0, id="all_zeros"),
    pytest.param([1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0], 3, id="interleaved"),
    pytest.param([], [], 0, id="empty"),
    pytest.param([0], [0], 0, id="single_zero"),
    pytest.param([42], [42], 1, id="single_nonzero"),
])
def test_move_zeros_to_end_parametrized(input_list, expected_list, expected_index):
    arr = input_list[:]
    result_index = move_zeros_to_end(arr)
    assert arr == expected_list
    assert result_index == expected_index


@pytest.mark.parametrize("matrix, expected_row", [
    pytest.param(
        [[0, 0, 1, 1],
         [0, 1, 1, 1],
         [0, 0, 0, 1],
         [1, 1, 1, 1],
         [0, 1, 1, 1]],
        3,
        id="classic"
    ),
    pytest.param(
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        0,
        id="all_zeros"
    ),
    pytest.param(
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]],
        0,
        id="all_ones_first"
    ),
    pytest.param(
        [[0, 1],
         [1, 1]],
        1,
        id="two_rows"
    ),
    pytest.param(
        [[0]],
        0,
        id="single_zero"
    ),
    pytest.param(
        [[1]],
        0,
        id="single_one"
    ),
    pytest.param(
        [],
        0,
        id="empty_matrix"
    ),
    pytest.param(
        [[0, 0, 1],
         [0, 1, 1],
         [0, 1, 1]], 
        1, 
        id="tie"
    ),
])
def test_find_row_with_most_ones(matrix, expected_row):
    assert find_row_with_most_ones(matrix) == expected_row


def test_find_row_with_most_ones_big_data():
    size = 10000
    matrix = [[0]*size for i in range(size)]
    matrix[size-1][size-1] = 1

    for i in range(50):
        assert find_row_with_most_ones(matrix) == 9999

    size = 10000
    matrix = [[1]*size for i in range(size)]
    matrix[0][0] = 0

    for i in range(50):
        assert find_row_with_most_ones(matrix) == 1


@pytest.mark.parametrize("input_arr, expected", [
    pytest.param([0], 1, id="self_loop"),
    pytest.param([1, 0], 1, id="two_cycle"),
    pytest.param([1, 2, 0], 1, id="three_cycle"),
    pytest.param([0, 1, 2], 3, id="three_self_loops"),
    pytest.param([1, 0, 3, 2], 2, id="two_2_cycles"),
    pytest.param([2, 0, 1, 4, 3], 2, id="mixed_cycles"),
    pytest.param([10, 6, 2, 9, 4, 0, 3, 8, 7, 1, 5], 5, id="mixed_cycles"),
    pytest.param([], 0, id="empty"),
])
def test_count_cycles(input_arr, expected):
    arr = input_arr[:]
    assert count_cycles(arr) == expected
