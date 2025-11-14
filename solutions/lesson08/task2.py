from typing import Callable, TypeVar

T = TypeVar("T")

def collect_statistic(
    statistics: dict[str, list[float, int]]
) -> Callable[[T], T]:
    
    # ваш код
    pass