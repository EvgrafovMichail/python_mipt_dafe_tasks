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

    if (
        not 1 <= retry_amount <= 100
        or not 0 < timeout_start <= timeout_max < 10
        or not 0 < backoff_scale < 10
    ):
        raise ValueError

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            current_delay = timeout_start
            for _ in range(retry_amount - 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if type(e) not in backoff_triggers:
                        raise e
                    else:
                        sleep(
                            min(current_delay, timeout_max) + uniform(0.0, 0.5)
                        )

                        current_delay *= backoff_scale
            return func(*args, **kwargs)

        return wrapper

    return decorator
