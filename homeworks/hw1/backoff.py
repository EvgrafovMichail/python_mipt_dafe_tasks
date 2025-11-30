from random import uniform
from time import sleep
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def backoff(
    retry_amount: int = 3,
    timeout_start: float = 0.5,
    timeout_max: float = 10.0,
    backoff_scale: float = 2.0,
    backoff_triggers: tuple[type[Exception]] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if (
        (0 < retry_amount < 101)
        and (0 < timeout_start < 10)
        and (0 < timeout_max < 10)
        and (0 < backoff_scale < 10)
    ):
        pass
    else:
        raise ValueError

    def repeating(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            stoptime = timeout_start

            while True:
                try:
                    return func(*args, **kwargs)

                except Exception as err:
                    if isinstance(err, backoff_triggers):
                        attempts += 1
                        if attempts > retry_amount:
                            raise
                        sleep(stoptime + uniform(0, 0.5))
                        stoptime *= backoff_scale
                        if stoptime > timeout_max:
                            stoptime = timeout_max
                    else:
                        raise

        return wrapper

    return repeating
