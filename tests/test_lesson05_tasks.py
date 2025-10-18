import pytest 

from solutions.lesson05.task1 import is_palindrome
from solutions.lesson05.task2 import are_anagrams
from solutions.lesson05.task3 import is_punctuation
from solutions.lesson05.task4 import unzip
from solutions.lesson05.task5 import reg_validator
from solutions.lesson05.task6 import simplify_path

@pytest.mark.parametrize("s, expected", [
    pytest.param("", True, id="empty_string"),
    pytest.param("a", True, id="single_char"),
    pytest.param("aa", True, id="two_same"),
    pytest.param("ab", False, id="two_different"),
    pytest.param("aba", True, id="odd_palindrome"),
    pytest.param("abba", True, id="even_palindrome"),
    pytest.param("abcba", True, id="long_odd_palindrome"),
    pytest.param("abccba", True, id="long_even_palindrome"),
    pytest.param("abc", False, id="not_palindrome"),
    pytest.param("Aa", True, id="case_sensitive_mismatch"),
    pytest.param("Racecar", True, id="real_word_case_sensitive"),
    pytest.param("aA", True, id="reverse_case"),
    pytest.param("abcdefedcba", True, id="long_true"),
    pytest.param("abcdefedcbx", False, id="long_false"),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected


@pytest.mark.parametrize("w1, w2, expected", [
    pytest.param("listen", "silent", True, id="classic_anagram"),
    pytest.param("evil", "vile", True, id="another_anagram"),
    pytest.param("a", "a", True, id="single_char_same"),
    pytest.param("A", "A", True, id="single_upper_same"),
    pytest.param("A", "a", False, id="case_sensitive_diff"),
    pytest.param("Listen", "Silent", False, id="mixed_case_not_anagram"),
    pytest.param("Aa", "aA", True, id="same_chars_permuted"),
    pytest.param("Ab", "ab", False, id="one_letter_case_diff"),
    pytest.param("abc", "cba", True, id="permuted_same_case"),
    pytest.param("abc", "Cba", False, id="case_breaks_anagram"),
    pytest.param("aabbcc", "abcabc", True, id="repeated_letters"),
    pytest.param("aabbcc", "aabbcd", False, id="extra_different_char"),
])
def test_are_anagrams_linear(w1, w2, expected):
    assert are_anagrams(w1, w2) == expected


@pytest.mark.parametrize("s, expected", [
    pytest.param("!!!", True, id="only_exclamations"),
    pytest.param("...?", True, id="dots_and_question"),
    pytest.param("", False, id="empty_string"),
    pytest.param("a", False, id="letter"),
    pytest.param("1", False, id="digit"),
    pytest.param(" ! ", False, id="space_inside"),
    pytest.param("!?.", True, id="symbols_only"),
    pytest.param("!a!", False, id="letter_in_middle"),
    pytest.param(" ", False, id="only_space"),
    pytest.param(".,;", True, id="commas_dots_semicolons"),
    pytest.param("", False, id="commas_dots_semicolons"),
])
def test_is_only_punctuation(s, expected):
    assert is_punctuation(s) == expected

@pytest.mark.parametrize("compressed, expected", [
    pytest.param("AbcD*4 ef GhI*2", "AbcDAbcDAbcDAbcDefGhIGhI", id="example"),
    pytest.param("a*3 b*2", "aaabb", id="simple_letters"),
    pytest.param("Hello", "Hello", id="star_one"),
    pytest.param("xyz", "xyz", id="no_compression"),
    pytest.param("", "", id="empty_input"),
    pytest.param("Test*2 Space", "TestTestSpace", id="mixed"),
    pytest.param("a*10", "aaaaaaaaaa", id="ten_a"),
    pytest.param("x y z", "xyz", id="three_plain"),
    pytest.param("Word word", "Wordword", id="case_sensitive"),
])
def test_decompress(compressed, expected):
    assert unzip(compressed) == expected

@pytest.mark.parametrize("regexp, s, expected", [
    pytest.param("d", "123", True, id="d_valid_number"),
    pytest.param("d", "0", True, id="d_zero"),
    pytest.param("d", "abc", False, id="d_letters_instead_of_digits"),
    pytest.param("d", "", False, id="d_empty_string"),
    pytest.param("w", "hello", True, id="w_lowercase_word"),
    pytest.param("w", "HelloWorld", True, id="w_mixed_case_word"),
    pytest.param("w", "hello123", False, id="w_word_with_digits"),
    pytest.param("w", "", False, id="w_empty_string"),
    pytest.param("s", "abc123", True, id="s_alphanum"),
    pytest.param("s", "ABC99", True, id="s_uppercase_and_digits"),
    pytest.param("s", "abc_123", False, id="s_contains_underscore"),
    pytest.param("s", "", False, id="s_empty_string"),
    pytest.param("d-d", "12-34", True, id="d_dash_d_valid"),
    pytest.param("d-d", "12--34", False, id="d_dash_d_double_dash"),
    pytest.param("d-d", "12-abc", False, id="d_dash_d_letters_after_dash"),
    pytest.param("d-d", "1234", False, id="d_dash_d_missing_dash"),
    pytest.param("w.w", "hi.there", True, id="w_dot_w_valid"),
    pytest.param("w.w", "hi..there", False, id="w_dot_w_double_dot"),
    pytest.param("w.w", "hi1.there", False, id="w_dot_w_digit_in_first_word"),
    pytest.param("s.s", "h1i.th32ere", True, id="s_dot_s_valid"),
    pytest.param("s.s", "hi4..t2here", False, id="s_dot_s_double_dot"),
    pytest.param("d-dw", "12-45abc", True, id="example_valid"),
    pytest.param("d-dw", "1-abs", False, id="example_second_part_not_digit"),
    pytest.param("d-dw", "1-b123r", False, id="example_letter_after_dash"),
    pytest.param("d-dw", "1--123vdg", False, id="example_double_dash"),
    pytest.param("d-dw", "123-456XYZ", True, id="d-dw_all_caps"),
    pytest.param("d-dw", "0-0a", True, id="d-dw_minimal_valid"),
    pytest.param("d@d", "5@7", True, id="d_at_d_valid"),
    pytest.param("d@d", "5@@7", False, id="d_at_d_double_at"),
    pytest.param("w s", "hi 123", True, id="w_space_s_valid"),
    pytest.param("w s", "hi123", False, id="w_space_s_missing_space"),
    pytest.param("w s", "hi 123!", False, id="w_space_s_extra_char_in_s"),
    pytest.param("", "", True, id="empty_regexp_empty_string"),
    pytest.param("", "a", False, id="empty_regexp_non_empty_string"),
    pytest.param("d", "", False, id="non_empty_regexp_empty_string"),
    pytest.param("d!", "5!", True, id="d_exclam_valid"),
    pytest.param("d!", "5", False, id="d_exclam_missing_exclam"),
    pytest.param("d!", "5!!", False, id="d_exclam_extra_exclam"),
    pytest.param("s", "a1", True, id="s_letter_digit"),
    pytest.param("s", "1a", True, id="s_digit_letter"),
    pytest.param("s", "a!1", False, id="s_contains_exclamation"),
    pytest.param("d-w-s", "123-abc-XY1Z23", True, id="d_w_s_valid"),
    pytest.param("d-w-s", "123-abc-XYZ_123", False, id="d_w_s_underscore_in_s"),
])
def test_match_pattern(regexp, s, expected):
    assert reg_validator(regexp, s) == expected


@pytest.mark.parametrize("path, expected", [
    pytest.param("/home/", "/home", id="trailing_slash"),
    pytest.param("/../", "", id="go_above_root"),
    pytest.param("/home//foo/", "/home/foo", id="double_slash"),
    pytest.param("/home/./foo/", "/home/foo", id="current_dir_dot"),
    pytest.param("/./././", "/", id="only_dots_and_slashes"),
    pytest.param("/a/./b/../../c/", "/c", id="complex_up_and_down"),
    pytest.param("/a/b/c/../../../", "/", id="back_to_root"),
    pytest.param("/", "/", id="root_only"),
    pytest.param("/.", "/", id="root_with_dot"),
    pytest.param("/..", "", id="root_with_double_dot"),
    pytest.param("/...", "/...", id="triple_dot_as_name"),
    pytest.param("/..a", "/..a", id="dot_dot_a_as_name"),
    pytest.param("/a.b/c.d", "/a.b/c.d", id="names_with_dots"),
    pytest.param("/a//b////c/d//././/..", "/a/b/c", id="messy_path"),
    pytest.param("/a/./b/./c/./d", "/a/b/c/d", id="dots_everywhere"),
    pytest.param("/a/./b/../../c/./d/", "/c/d", id="up_down_with_dots"),
    pytest.param("/../foo", "", id="up_then_valid"),
    pytest.param("/../../foo", "", id="multiple_up_then_valid"),
    pytest.param("/../../../", "", id="three_up_from_root"),
    pytest.param("/home/foo/./../../../", "", id="too_many_up"),
    pytest.param("/_a.b/c__1/..", "/_a.b", id="names_with_underscores_and_dots"),
])
def test_simplify_path(path, expected):
    assert simplify_path(path) == expected