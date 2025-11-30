from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        cap = int(round(capacity))
    except Exception:
        raise TypeError

    if cap < 1:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}
        first = None
        last = None

        def link_new(signature, value):
            nonlocal first, last
            cache[signature] = [value, last, None]
            if last is not None:
                cache[last][2] = signature
            else:
                first = signature
            last = signature

        def unlink(signature):
            nonlocal first, last
            _, p, n = cache[signature]

            if p is None:
                first = n
            else:
                cache[p][2] = n

            if n is None:
                last = p
            else:
                cache[n][1] = p

            del cache[signature]

        def make_mru(signature):
            if signature == last:
                return
            v = cache[signature][0]
            unlink(signature)
            link_new(signature, v)

        def wrapper(*args, **kwargs):
            signature = args + tuple(sorted(kwargs.items()))
            if signature in cache:
                make_mru(signature)
                return cache[signature][0]

            result = func(*args, **kwargs)

            if len(cache) >= cap:
                unlink(first)

            link_new(signature, result)
            return result

        return wrapper

    return decorator
