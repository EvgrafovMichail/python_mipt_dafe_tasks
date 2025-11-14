import math
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def get_statistic(func):
        def wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            taken = time.time() - time_start

            if func.__name__ in statistics:
                calls = statistics[func.__name__][1]
                avg = statistics[func.__name__][0]

                statistics[func.__name__][0] = (taken + avg * calls) / (calls + 1)
                statistics[func.__name__][1] = calls + 1
            else:
                statistics[func.__name__] = [taken, 1]

            return result

        wrapper.__name__ = func.__name__
        return wrapper

    return get_statistic


statistics: list[str, list[float, int]] = {}


@collect_statistic(statistics)
def func1() -> None:
    time.sleep(2)


@collect_statistic(statistics)
def func2() -> None:
    time.sleep(1)


for _ in range(3):
    func1()

for i in range(6):
    func2()

eps = 1e-3

print(statistics)
assert statistics[func1.__name__][1] == 3
assert statistics[func2.__name__][1] == 6
assert math.isclose(statistics[func1.__name__][0], 2, abs_tol=eps)
assert math.isclose(statistics[func2.__name__][0], 1, abs_tol=eps)
