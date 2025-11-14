import pytest 
import math
import time

from solutions.lesson08.task1 import make_averager
from solutions.lesson08.task2 import collect_statistic

def test_make_averager():
    get_avg = make_averager(2)

    assert math.isclose(get_avg(1), 1)
    assert math.isclose(get_avg(2), 1.5)
    assert math.isclose(get_avg(3), 2.5)
    assert math.isclose(get_avg(-3), 0)
    assert math.isclose(get_avg(5), 1)
    assert math.isclose(get_avg(5), 5)

def test_make_averager2():
    get_avg = make_averager(5)

    assert math.isclose(get_avg(1), 1)
    assert math.isclose(get_avg(2), 1.5)
    assert math.isclose(get_avg(3), 2)
    assert math.isclose(get_avg(4), 2.5)
    assert math.isclose(get_avg(5), 3)
    assert math.isclose(get_avg(-5), 1.8)
    assert math.isclose(get_avg(-7), 0)
    assert math.isclose(get_avg(-2), -1)

def test_collect_statistic():
    statistics: list[str, list[float, int]] = {}

    @collect_statistic(statistics)
    def func1() -> None:
        time.sleep(0.05)

    @collect_statistic(statistics)
    def func2() -> None:
        time.sleep(0.1)
    
    for _ in range(3):
        func1()

    for i in range(6):
        func2()

    eps = 1e-3

    assert statistics[func1.__name__][1] == 3
    assert statistics[func2.__name__][1] == 6
    assert math.isclose(statistics[func1.__name__][0], 0.05, abs_tol=eps)
    assert math.isclose(statistics[func2.__name__][0], 0.1, abs_tol=eps)


def test_collect_statistic_inout():
    statistics: list[str, list[float, int]] = {}

    @collect_statistic(statistics)
    def func(a, b, *, c, d):
        return a + b + c + d
    
    assert func(1, 2, c=3, d=4) == 10
    assert statistics[func.__name__][1] == 1

def test_collect_statistic_count_call():
    statistics: list[str, list[float, int]] = {}

    def func_fab():
        count_call = 0

        @collect_statistic(statistics)
        def func():
            nonlocal count_call
            if count_call > 0:
                raise RuntimeError("The function must be called once.")
            count_call += 1

        return func
    
    func = func_fab()
    func()
    assert statistics[func.__name__][1] == 1