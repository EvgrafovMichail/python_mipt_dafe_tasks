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

    def decorator(func):
        timeout = timeout_start
        jitter_time = uniform(0, 0.5)
        def wrapper(*args, **kwargs):
            for i in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as exc:
                    nonlocal timeout
                    if timeout > timeout_max:
                        raise TimeoutError
                    sleep(timeout + jitter_time)
                    timeout *= backoff_scale
            raise exc("no attempts left")
        return wrapper
    return decorator

attempts = 0
timeout_max = 4
retry_amount = 4
timeouts = [1, 2, 4, 4]
@backoff(
        retry_amount=retry_amount,
        timeout_start=1,
        timeout_max=timeout_max,
        backoff_scale=2.0
    )
def func():
    global attempts
    attempts += 1
    if attempts < retry_amount:
        raise ConnectionError("Ошибка подключения")
    return "успех"

print(func())