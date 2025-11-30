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

    if retry_amount < 1:
        raise ValueError("максимальное количество попыток выполнения функции должно быть положительно")
    if timeout_start <= 0 or timeout_max <= 0:
        raise ValueError("Время - деньги")
    if backoff_scale <= 0:
        raise ValueError("Кэфы горят, надо лить")

    def deko(func: Callable[P, R]):
        def wrapper(*args, **kwargs):
            exceptionn = None
            timeout = timeout_start
            
            for tryy in range(retry_amount):
                try:
                    return func(*args, **kwargs)
                except backoff_triggers as z:
                    exceptionn = z

                    if tryy == retry_amount - 1:
                        raise exceptionn
                    
                    jiter = uniform(0, 0.5)
                    time = min(timeout + jiter, timeout_max)

                    sleep(time)

                    timeout = min(timeout * backoff_scale, timeout_max)

        return wrapper
        
    return deko