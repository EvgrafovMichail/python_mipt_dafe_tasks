import pytest

from solutions.lesson02.task1 import get_factorial
from solutions.lesson02.task2 import get_doubled_factorial
from solutions.lesson02.task3 import get_amount_of_ways_to_climb
from solutions.lesson02.task4 import get_multiplications_amount
from solutions.lesson02.task5 import get_gcd
from solutions.lesson02.task6 import get_sum_of_prime_divisors
from solutions.lesson02.task7 import is_palindrome

@pytest.mark.parametrize(
    "num, result_expected", 
    (
        pytest.param(
            0,
            1,
            id="zero",
        ),
        pytest.param(
            1,
            1,
            id="one",
        ),
        pytest.param(
            2,
            2,
            id="lowest-factorial",
        ),
        pytest.param(
            3,
            6,
            id="middle-factorial",
        ),
        pytest.param(
            20,
            2432902008176640000,
            id="greatest-factorial",
        ),
    ),
)
def test_get_factorial(num: int, result_expected: int) -> None:
    assert get_factorial(num) == result_expected


@pytest.mark.parametrize(
    "num, result_expected", 
    (
        pytest.param(
            0,
            1,
            id="zero",
        ),
        pytest.param(
            1,
            1,
            id="one",
        ),
        pytest.param(
            2,
            2,
            id="two",
        ),
        pytest.param(
            3,
            3,
            id="three",
        ),
        pytest.param(
            4,
            8,
            id="four",
        ),
        pytest.param(
            20,
            3715891200,
            id="twenty",
        ),
    ),
)
def test_get_doubled_factorial(num: int, result_expected: int) -> None:
    assert get_doubled_factorial(num) == result_expected


@pytest.mark.parametrize(
    "num, result_expected", 
    (
        pytest.param(
            1,
            1,
            id="n=1 -> res=1",
        ),
        pytest.param(
            2,
            2,
            id="n=2 -> res=2",
        ),
        pytest.param(
            3,
            3,
            id="n=3 -> res=3",
        ),
        pytest.param(
            4,
            5,
            id="n=4 -> res=5",
        ),
        pytest.param(
            20,
            10946,
            id="n=20 -> res=10946",
        ),
        pytest.param(
            45,
            1836311903,
            id="n=45 -> res=1836311903",
        ),
    ),
)
def test_get_amount_of_ways_to_climb(
    num: int,
    result_expected: int,
) -> None:
    assert get_amount_of_ways_to_climb(num) == result_expected


@pytest.mark.parametrize(
    "num, result_expected", 
    (
        pytest.param(
            1,
            0,
            id="one",
        ),
        pytest.param(
            2,
            1,
            id="two",
        ),
        pytest.param(
            5,
            3,
            id="five",
        ),
        pytest.param(
            999,
            16,
            id="nine-hundred-ninety-nine",
        ),
        pytest.param(
            1000,
            14,
            id="one-thousand",
        ),
    ),
)
def test_get_multiplications_amount(
    num: int,
    result_expected: int,
) -> None:
    assert get_multiplications_amount(num) == result_expected


@pytest.mark.parametrize(
    "num1, num2, result_expected", 
    (
        pytest.param(
            1,
            1,
            1,
            id="one-and-one",
        ),
        pytest.param(
            2,
            1,
            1,
            id="two-and-one",
        ),
        pytest.param(
            4,
            2,
            2,
            id="four-and-two",
        ),
        pytest.param(
            2,
            4,
            2,
            id="two-and-four",
        ),
        pytest.param(
            75,
            125,
            25,
            id="seventy-five-and-one-hundred-twenty-five",
        ),
        pytest.param(
            125,
            75,
            25,
            id="one-hundred-twenty-five-and-seventy-five",
        ),
        pytest.param(
            75,
            75,
            75,
            id="seventy-five-and-seventy-five",
        ),
        pytest.param(
            125,
            73,
            1,
            id="one-hundred-twenty-five-and-seventy-three",
        ),
        pytest.param(
            73,
            125,
            1,
            id="seventy-three-and-one-hundred-twenty-five",
        ),
    ),
)
def test_get_gcd(
    num1: int,
    num2: int,
    result_expected: int,
) -> None:
    assert get_gcd(num1, num2) == result_expected


@pytest.mark.parametrize(
    "num, result_expected", 
    (
        pytest.param(
            1,
            0,
            id="one",
        ),
        pytest.param(
            2,
            2,
            id="two",
        ),
        pytest.param(
            5,
            5,
            id="five",
        ),
        pytest.param(
            12,
            5,
            id="twelve",
        ),
        pytest.param(
            13,
            13,
            id="thirteen",
        ),
        pytest.param(
            10**10 - 1,
            9417,
            id="ten-billion-minus-one",
        ),
        pytest.param(
            10**10,
            7,
            id="ten-billion",
        ),
    ),
)
def test_get_sum_of_prime_divisors(num: int, result_expected: int) -> None:
    assert get_sum_of_prime_divisors(num) == result_expected


@pytest.mark.parametrize(
    "num, result_expected", 
    (
        pytest.param(
            -10**10,
            False,
            id="negative-ten-billion",
        ),
        pytest.param(
            -1,
            False,
            id="negative-one",
        ),
        pytest.param(
            0,
            True,
            id="zero",
        ),
        pytest.param(
            1,
            True,
            id="one",
        ),
        pytest.param(
            121,
            True,
            id="one-hundred-twenty-one",
        ),
        pytest.param(
            123,
            False,
            id="one-hundred-twenty-three",
        ),
        pytest.param(
            12211221,
            True,
            id="twelve-million-two-hundred-eleven-thousand-two-hundred-twenty-one",
        ),
        pytest.param(
            10**10,
            False,
            id="ten-billion",
        ),
    ),
)
def test_is_palindrome(num: int, result_expected: bool) -> None:
    assert is_palindrome(num) == result_expected

