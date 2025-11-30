from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    Any,
)

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Параметризованный декоратор для реализации LRU-кеширования.

    Args:
        capacity: целое число, максимальный возможный размер кеша.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        TypeError, если capacity не может быть округлено и использовано
            для получения целого числа.
        ValueError, если после округления capacity - число, меньшее 1.
    """
    # ваш код
    from typing import Callable, ParamSpec, TypeVar, Any

P = ParamSpec("P")
R = TypeVar("R")


def lru_cache(capacity: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    try:
        capacity = round(capacity)
    except Exception:
        raise TypeError("capacity must be compatible with round()")
    if capacity < 1:
        raise ValueError("capacity must be >= 1")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        class _Node:
            __slots__ = ("key", "value", "prev", "next")
            def __init__(self, key: Any, value: Any):
                self.key = key
                self.value = value
                self.prev: _Node | None = None
                self.next: _Node | None = None

        head = _Node(None, None)
        tail = _Node(None, None)
        head.next = tail
        tail.prev = head

        cache: dict[tuple, _Node] = {}

        def _remove(node: _Node) -> None:
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev

        def _add_to_head(node: _Node) -> None:
            node.prev = head
            node.next = head.next
            head.next.prev = node
            head.next = node

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                node = cache[key]
                _remove(node)
                _add_to_head(node)
                return node.value
            else:
                result = func(*args, **kwargs)
                new_node = _Node(key, result)
                cache[key] = new_node
                _add_to_head(new_node)
                if len(cache) > capacity:
                    lru = tail.prev
                    _remove(lru)
                    del cache[lru.key]
                return result

        return wrapper

    return decorator
