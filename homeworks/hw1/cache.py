from typing import (
    Callable,
    ParamSpec,
    TypeVar,
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
    try:
        capacity = round(capacity)
    except (TypeError, ValueError) as e:
        raise TypeError
    
    if capacity < 1:
        raise ValueError

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        class Node:
            def __init__(self, key, value):
                self.key = key
                self.value = value
                self.prev = None
                self.next = None

        cache = {}
        head = Node(None, None)
        tail = Node(None, None)
        head.next = tail
        tail.prev = head

        def remove_node(node: Node):
            """Удаляет узел из двусвязного списка"""
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

        def add_to_front(node: Node):
            """Добавляет узел в начало списка (после head)"""
            first_node = head.next
            head.next = node
            node.prev = head
            node.next = first_node
            first_node.prev = node

        def move_to_front(node: Node):
            """Перемещает узел в начало списка"""
            remove_node(node)
            add_to_front(node)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                node = cache[key]
                move_to_front(node)
                return node.value
            else:
                result = func(*args, **kwargs)
                
                new_node = Node(key, result)
                
                if len(cache) >= capacity:
                    lru_node = tail.prev
                    remove_node(lru_node)
                    del cache[lru_node.key]
                
                add_to_front(new_node)
                cache[key] = new_node
                
                return result

        return wrapper

    return decorator