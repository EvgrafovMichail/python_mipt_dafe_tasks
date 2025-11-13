from typing import Callable, TypeVar, Any

import time

T = TypeVar("T")


def collect_statistic(statistics: dict[str, list[float, int]]) -> Callable[[T], T]:
    def function(func: Callable[T]):
        def tester(test: Any, body: Any):
            start = time.time
            a = func(test, body)
            end = time.time
            timee = end - start

            func_name = func.__name__

            if func_name not in statistics:
                statistics[func_name] = [timee, 1]
            else:
                arg1, count1 = statistics[func_name]
                count2 = count1 + 1
                arg2 = (arg1 * count1 + timee) / count2
                statistics[func_name] = [arg2, count2]

            return a

        return tester

    return function
