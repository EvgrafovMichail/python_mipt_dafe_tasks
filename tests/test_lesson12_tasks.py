import sys

import pytest

from solutions.lesson12.task1 import chunked
from solutions.lesson12.task2 import circle
from solutions.lesson12.task3 import FileOut


def finite_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def infinite_generator():
    i = 1
    while True:
        yield i
        i += 1


@pytest.mark.parametrize(
    "iter_obj, size, expected",
    [
        pytest.param([1, 2, [3], "4", 5], 2, [(1, 2), ([3], "4"), (5,)], id="list"),
        pytest.param([1, 2, [3], "4", 5], 1, [(1,), (2,), ([3],), ("4",), (5,)], id="list-size-1"),
        pytest.param("abcdefg", 3, [("a", "b", "c"), ("d", "e", "f"), ("g",)], id="str"),
        pytest.param({1, 2, 3, 4, 5}, 2, [(1, 2), (3, 4), (5,)], id="set"),
        pytest.param(map(lambda x: x, [1, 2, 3, 4, 5]), 2, [(1, 2), (3, 4), (5,)], id="iterator"),
        pytest.param(finite_generator(), 2, [(1, 2), (3, 4), (5,)], id="finite_generator"),
    ],
)
def test_chunked(iter_obj, size, expected):
    gen = chunked(iter_obj, size)

    assert list(gen) == expected
    with pytest.raises(StopIteration):
        next(gen)


def test_chunked_infinite_generator():
    gen = chunked(infinite_generator(), 5)
    expected = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]

    assert [next(gen) for _ in range(len(expected))] == expected


def test_empty_chunked():
    gen = chunked([], 2)

    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize(
    "iter_obj, expected",
    [
        pytest.param([1, 2, [3]], [1, 2, [3], 1, 2, [3], 1, 2], id="list"),
        pytest.param("aB", ["a", "B", "a", "B", "a"], id="str"),
        pytest.param({1, 2, 3}, [1, 2, 3, 1, 2, 3, 1, 2], id="set"),
        pytest.param({1: "a", 2: "b", 3: "c"}, [1, 2, 3, 1, 2, 3, 1, 2], id="dict"),
        pytest.param(map(lambda x: x, [1, 2, 3]), [1, 2, 3, 1, 2, 3, 1, 2], id="iterator"),
        pytest.param(
            finite_generator(), [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2], id="finite_generator"
        ),
        pytest.param(infinite_generator(), [1, 2, 3, 4, 5, 6, 7, 8], id="infinite_generator"),
    ],
)
def test_circle(iter_obj, expected):
    gen = circle(iter_obj)

    assert [next(gen) for _ in range(len(expected))] == expected


def test_empty_circle():
    gen = circle([])

    with pytest.raises(StopIteration):
        next(gen)


def test_file_out(tmp_path):
    stdout = sys.stdout
    file_path = tmp_path / "test.txt"

    print("zero")

    with FileOut(file_path) as manager:
        print("first")

    with open(file_path, "r") as file:
        assert file.readlines() == ["first\n"]

    assert stdout == sys.stdout
    print("second")

    with open(file_path, "r") as file:
        assert file.readlines() == ["first\n"]

    with manager:
        print("third")

    assert stdout == sys.stdout
    with open(file_path, "r") as file:
        assert file.readlines() == ["third\n"]


def test_file_out2(tmp_path):
    stdout = sys.stdout
    file_path1 = tmp_path / "test1.txt"
    file_path2 = tmp_path / "test2.txt"

    print("zero")

    with FileOut(file_path1):
        print("first")

    assert stdout == sys.stdout
    with open(file_path1, "r") as file:
        assert file.readlines() == ["first\n"]

    print("second")

    with open(file_path1, "r") as file:
        assert file.readlines() == ["first\n"]

    with FileOut(file_path2):
        print("third")

    assert stdout == sys.stdout
    with open(file_path1, "r") as file:
        assert file.readlines() == ["first\n"]

    with open(file_path2, "r") as file:
        assert file.readlines() == ["third\n"]


def test_file_out_exception(tmp_path):
    stdout = sys.stdout
    file_path = tmp_path / "test.txt"

    print("zero")

    with pytest.raises(ValueError):
        with FileOut(file_path):
            print("first")
            raise ValueError

    assert stdout == sys.stdout
    print("second")
    with open(file_path, "r") as file:
        assert file.readlines() == ["first\n"]
