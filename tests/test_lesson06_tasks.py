import pytest 

from solutions.lesson06.task1 import int_to_roman
from solutions.lesson06.task2 import get_len_of_longest_substring
from solutions.lesson06.task3 import is_there_any_good_subarray
from solutions.lesson06.task4 import count_unique_words


@pytest.mark.parametrize("num, expected", [
    pytest.param(1, "I", id="one"),
    pytest.param(2, "II", id="two"),
    pytest.param(3, "III", id="three"),
    pytest.param(4, "IV", id="four"),
    pytest.param(5, "V", id="five"),
    pytest.param(6, "VI", id="six"),
    pytest.param(9, "IX", id="nine"),
    pytest.param(10, "X", id="ten"),
    pytest.param(11, "XI", id="eleven"),
    pytest.param(14, "XIV", id="fourteen"),
    pytest.param(19, "XIX", id="nineteen"),
    pytest.param(27, "XXVII", id="twenty_seven"),
    pytest.param(40, "XL", id="forty"),
    pytest.param(44, "XLIV", id="forty_four"),
    pytest.param(50, "L", id="fifty"),
    pytest.param(58, "LVIII", id="fifty_eight"),
    pytest.param(90, "XC", id="ninety"),
    pytest.param(99, "XCIX", id="ninety_nine"),
    pytest.param(100, "C", id="hundred"),
    pytest.param(400, "CD", id="four_hundred"),
    pytest.param(500, "D", id="five_hundred"),
    pytest.param(900, "CM", id="nine_hundred"),
    pytest.param(1000, "M", id="thousand"),
    pytest.param(1994, "MCMXCIV", id="mcmxciv"),
    pytest.param(3999, "MMMCMXCIX", id="max_value"),
    pytest.param(2023, "MMXXIII", id="current_year"),
    pytest.param(1984, "MCMLXXXIV", id="classic"),
])
def test_int_to_roman(num, expected):
    assert int_to_roman(num) == expected

@pytest.mark.parametrize("s, expected", [
    pytest.param("", 0, id="empty_string"),
    pytest.param("a", 1, id="single_char"),
    pytest.param("aa", 1, id="two_same_chars"),
    pytest.param("ab", 2, id="two_different_chars"),
    pytest.param("abcabcbb", 3, id="classic_example_abc"),
    pytest.param("bbbbb", 1, id="all_same"),
    pytest.param("pwwkew", 3, id="pwwkew_example"),
    pytest.param("abcdef", 6, id="all_unique"),
    pytest.param("abcabcbbxyz", 4, id="long_tail_unique"),
    pytest.param("aab", 2, id="aab"),
    pytest.param("dvdf", 3, id="dvdf"),
    pytest.param(" ", 1, id="single_space"),
    pytest.param("a b c", 3, id="letters_and_spaces_unique"),
    pytest.param("a b a", 3, id="space_in_middle_with_repeat"),
    pytest.param("1234567890", 10, id="digits_all_unique"),
    pytest.param("112233", 2, id="repeating_digits"),
    pytest.param("abcdefghijklmnopqrstuvwxyz", 26, id="all_lowercase_letters"),
    pytest.param("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ", 63, id="max_unique_set"),
    pytest.param("a" * 10000, 1, id="ten_thousand_same"),
    pytest.param("abc" * 3333 + "d", 4, id="long_repeating_with_new_char"),
])
def test_get_len_of_longest_substring(s, expected):
    assert get_len_of_longest_substring(s) == expected

@pytest.mark.parametrize("nums, k, expected", [
    pytest.param([23, 2, 4, 6, 7], 6, True, id="subarray_2_4_sum_6"),
    pytest.param([23, 2, 6, 4, 7], 6, True, id="total_sum_42_div_by_6"),
    pytest.param([23, 2, 6, 4, 7], 13, False, id="no_valid_subarray"),
    pytest.param([0, 0], 1, True, id="two_zeros_any_k"),
    pytest.param([1, 0], 2, False, id="length_2_sum_1_not_div_by_2"),
    pytest.param([1, 2, 3], 5, True, id="subarray_2_3_sum_5"),
    pytest.param([1], 1, False, id="single_element_too_short"),
    pytest.param([5, 0, 0], 3, True, id="zeros_after_nonzero"),
    pytest.param([1, 2], 3, True, id="exact_sum_equals_k"),
    pytest.param([1, 2], 4, False, id="sum_not_divisible_by_k"),
    pytest.param([0], 1, False, id="single_zero_too_short"),
    pytest.param([1, 0, 2], 2, True, id="subarray_0_2_sum_2"),
    pytest.param([4, 2, 4], 6, True, id="first_two_sum_6"),
    pytest.param([1, 1, 1], 2, True, id="first_two_ones_sum_2"),
    pytest.param([1, 2, 4, 8], 8, False, id="no_subarray_divisible_by_8"),
    pytest.param([0, 1, 0], 2, False, id="zeros_with_one_sum_1"),
    pytest.param([0, 1, 0, 0], 2, True, id="last_two_zeros_sum_0_div_by_any"),
])
def test_is_there_any_good_subarray(nums, k, expected):
    assert is_there_any_good_subarray(nums, k) == expected


import pytest

@pytest.mark.parametrize("text, expected", [
    pytest.param("", 0, id="empty_string"),
    pytest.param("   ", 0, id="only_spaces"),
    pytest.param("hello", 1, id="single_word"),
    pytest.param("Hello hello", 1, id="case_insensitive"),
    pytest.param("Hello, world!", 2, id="punctuation_around"),
    pytest.param("Hello, hello, world!", 2, id="duplicates_with_punct"),
    pytest.param("The quick brown fox jumps over the lazy dog.", 8, id="classic_pangram"),
    pytest.param("!!! ???", 0, id="only_punctuation"),
    pytest.param("word1 word2 word1", 2, id="digits_in_words"),
    pytest.param("Don't stop believing!", 3, id="apostrophe_inside"),
    pytest.param("   Hello ,   World !   ", 2, id="extra_whitespace"),
    pytest.param("A a A a", 1, id="repeated_case_variants"),
    pytest.param("word... word!!!", 1, id="multiple_punct_at_end"),
    pytest.param("123 456 123", 2, id="numbers_as_words"),
])
def test_count_unique_words(text, expected):
    assert count_unique_words(text) == expected