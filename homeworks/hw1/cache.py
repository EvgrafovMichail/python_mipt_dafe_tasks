from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        maxsize = round(capacity)
    except Exception:
        raise TypeError

    if maxsize < 1:
        raise ValueError

    def trying(func):
        nonlocal maxsize
        argslist = []

        def wrapper(*args):
            nonlocal argslist, maxsize
            for pairs in argslist:
                if pairs[0] == args:
                    argslist.remove(pairs)
                    argslist = [pairs] + argslist
                    return pairs[1]
            result = func(args)
            argslist = [(args, result)] + argslist
            if len(argslist) > maxsize:
                argslist.pop()
            return result

        return wrapper

    return trying
