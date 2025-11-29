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
    """
    Параметризованный декоратор для повторных запусков функций.

    Args:
        retry_amount: максимальное количество попыток выполнения функции;
        timeout_start: начальное время ожидания перед первой повторной попыткой (в секундах);
        timeout_max: максимальное время ожидания между попытками (в секундах);
        backoff_scale: множитель, на который увеличивается задержка после каждой неудачной попытки;
        backoff_triggers: кортеж типов исключений, при которых нужно выполнить повторный вызов.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        ValueError, если были переданы невозможные аргументы.
    """
    if not (
        isinstance(retry_amount, int)
        and retry_amount > 0
        and isinstance(timeout_start, (float, int))
        and timeout_start > 0
        and isinstance(timeout_max, (float, int))
        and timeout_max > 0
        and isinstance(backoff_scale, (float, int))
        and backoff_scale > 0
    ):
        raise ValueError("Invalid arguments")

    def wrapper(func):
        curr_timeout = timeout_start
        exception = None

        def recall(*args, **kwargs):
            nonlocal curr_timeout, exception
            for i in range(retry_amount):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as exc:
                    exception = exc

                    if isinstance(exc, backoff_triggers):
                        sleep(curr_timeout + uniform(0, 0.5))
                        curr_timeout = curr_timeout * backoff_scale
                        if curr_timeout > timeout_max:
                            curr_timeout = timeout_max

                    else:
                        raise exc
            raise exception

        return recall

    return wrapper
