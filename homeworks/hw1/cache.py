from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    capacity = round(capacity)

    if not isinstance(capacity, int):
        raise TypeError

    if capacity < 1:
        raise ValueError

    def decorator(func):
        cache = {}
        head = None
        tail = None

        def _append(key, value):
            nonlocal head, tail

            cache[key] = (value, tail, None)

            if tail is not None:
                value, prev, _ = cache[tail]
                cache[tail] = (value, prev, key)

            if head is None:
                head = key

            tail = key

        def _remove(key):
            nonlocal head, tail

            if key not in cache:
                return

            _, prev_key, next_key = cache[key]

            if prev_key is not None:
                prev_val, prev_prev, _ = cache[prev_key]
                cache[prev_key] = (prev_val, prev_prev, next_key)
            else:
                head = next_key
                prev_prev = None

            if next_key is not None:
                next_val, _, next_next = cache[next_key]
                cache[next_key] = (next_val, prev_key, next_next)
            else:
                tail = prev_key
                next_next = None

            del cache[key]

        def _move_to_tail(key):
            if key == tail:
                return

            value, _, _ = cache[key]
            _remove(key)
            _append(key, value)

        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items())) if kwargs else args

            if key in cache:
                _move_to_tail(key)
                value, _, _ = cache[key]
                return value
            else:
                result = func(*args, **kwargs)

                if len(cache) >= capacity:
                    _remove(head)

                _append(key, result)
                return result

        return wrapper

    return decorator
