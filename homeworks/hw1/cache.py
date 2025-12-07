from functools import wraps
from random import uniform
from time import sleep
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers:
                    if attempt == retry_amount - 1:
                        raise
                    timeout = min(
                        timeout_start * (backoff_scale**attempt) + uniform(0, 0.5),
                        timeout_max
                    )
                    sleep(timeout)
            raise Exception("Max retries exceeded")

        return wrapper

    return decorator


@backoff(retry_amount=2, timeout_start=0.1)
def example_function(x: int) -> int:
    return x * 2


def main() -> None:
    result = example_function(5)


if __name__ == "__main__":
    main()