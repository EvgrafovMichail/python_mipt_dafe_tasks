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

    # ваш код
    if not (isinstance(retry_amount, int) and 1 <= retry_amount <= 100):
        raise ValueError("retry_amount должен быть целым числом от 1 до 100")
    for name, value, lim in (
        ("timeout_start", timeout_start, (0, 10)),
        ("timeout_max", timeout_max, (0, 10)),
        ("backoff_scale", backoff_scale, (0, 10)),
    ):
        if not (isinstance(value, (int, float)) and lim[0] < value < lim[1]):
            raise ValueError(f"{name} должен быть в интервале {lim}")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            delay = timeout_start
            last_exc: Exception | None = None

            for attempt in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as exc:
                    last_exc = exc
                    if attempt == retry_amount - 1:
                        break
                    sleep(min(delay, timeout_max) + uniform(0, 0.5))
                    delay *= backoff_scale

            assert last_exc is not None
            raise last_exc

        return wrapper

    return decorator
