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

    if any([v <= 0 for v in [retry_amount, timeout_start, timeout_max, backoff_scale]]):
        raise ValueError("retry_amount, timeout_start, timeout_max, backoff_scale must be positive")

    def decorator(func: Callable[[P], R]) -> Callable[[P], R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            timeout_current = timeout_start
            last_exc = None

            for attempt in range(1, retry_amount + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if not any([isinstance(e, trigger) for trigger in backoff_triggers]):
                        raise e
                    else:
                        if attempt == retry_amount:
                            last_exc = e
                            break

                        jitter = uniform(0, 0.5)
                        sleep(min(timeout_current, timeout_max) + jitter)
                        timeout_current *= backoff_scale

            raise last_exc

        return wrapper

    return decorator
