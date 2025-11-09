from typing import Callable
from collections import deque
import math


def make_averager(accumulation_period: int) -> Callable[[float], float]:
    summa = 0
    number = 0
    deq = deque()

    def get_avg(value: float) -> float:
        nonlocal summa, number, deq
        if number < accumulation_period:
            number += 1
            print(number)
        else:
            summa -= deq.popleft()
            print(number)
        summa += value
        deq.append(value)
        print(deq)
        return summa / number

    return get_avg
