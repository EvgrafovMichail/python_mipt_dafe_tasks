from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        capacity = round(capacity)
    except Exception:
        raise TypeError()

    if capacity < 1:
        raise ValueError()

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = {}  # key -> {"value": value, "prev": prev_key, "next": next_key}
        first = None
        last = None
        curr_len = 0

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            nonlocal first, last, curr_len
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                if first != key:
                    prev_key = cache[key]["prev"]
                    next_key = cache[key]["next"]
                    if key == last:
                        last = prev_key
                    if prev_key is not None:
                        cache[prev_key]["next"] = next_key
                    if next_key is not None:
                        cache[next_key]["prev"] = prev_key
                    cache[first]["prev"] = key
                    cache[key]["prev"] = None
                    cache[key]["next"] = first
                    first = key
                return cache[key]["value"]
            else:
                if curr_len == capacity:
                    if (
                        capacity == 1
                    ):  # отдельно обрабатываем capacity = 1, чтобы избежать TypeError
                        del cache[first]
                        cache[key] = {"value": func(*args, **kwargs), "prev": None, "next": None}
                        first = key
                        last = key
                    else:
                        old_last = last
                        last = cache[last][
                            "prev"
                        ]  # меняем last на предыдущий элемент текущего last
                        del cache[
                            old_last
                        ]  # удаляем последний элемент (он "next" для предпоследнего)
                        cache[last]["next"] = None
                        cache[first]["prev"] = key
                        cache[key] = {"value": func(*args, **kwargs), "prev": None, "next": first}
                        first = key
                else:  # если словарь еще не переполнился, увеличиваем его длину
                    curr_len += 1
                    if first is None:  # случай пустого словаря (вызова первой функции)
                        cache[key] = {"value": func(*args, **kwargs), "prev": None, "next": None}
                        first = key
                        last = key
                    else:
                        cache[first]["prev"] = key
                        cache[key] = {"value": func(*args, **kwargs), "prev": None, "next": first}
                        first = key
                return cache[key]["value"]

        return wrapper

    return decorator
