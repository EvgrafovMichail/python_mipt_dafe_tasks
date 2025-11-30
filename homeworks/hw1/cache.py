import functools
from typing import (
    Any,
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if not isinstance(capacity, (int, float)):
        raise TypeError("capacity must be int")

    if round(capacity) <= 1:
        raise ValueError("capacity must be more than 1")

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        data = {}
        try:
            argcount = func.__code__.co_argcount
            default_value = func.__defaults__
            if default_value is None:
                default_value = ()
            per_names = func.__code__.co_varnames[:argcount]

        except AttributeError:
            @functools.wraps(func)
            def inner(*args, **kwargs):
                args = tuple(args)

                if args in data.keys():
                    item = data[args]
                    del data[args]
                    data[args] = item
                    return data[args]

                else:
                    if len(data) == capacity:
                        del data[next(iter(data))]
                    data[args] = func(*args, **kwargs)
                    return data[args]

        else :
            @functools.wraps(func)
            def inner(*args: P.args, **kwargs: P.kwargs) -> Any:
                key = []

                if args:
                    key += list(args)

                if kwargs:
                    for name in per_names:
                        if name in kwargs:
                            key.append(kwargs[name])

                if len(key) < argcount:
                    for value in default_value[-(argcount - len(args) - len(kwargs)) :]:
                        key.append(value)

                key = tuple(key)

                # проверка наличия значения для аргумента в базе
                if data.get(key) is None:
                    # проверка переполненности базы
                    if len(data) >= capacity:
                        del data[next(iter(data))]

                    data[key] = func(*args, **kwargs)

                else:
                    # обновляем приоритет
                    value_func_by_args = data[key]
                    del data[key]
                    data[key] = value_func_by_args

                return data[key]

        return inner

    return wrapper
