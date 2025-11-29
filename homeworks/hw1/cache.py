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
        new_capacity = round(capacity)
    except Exception:
        raise TypeError from None
    else:
        if new_capacity < 1:  # < 1 или <= 1 ???
            raise ValueError from None

    dictionary = {}

    def decorator(func: Callable[P, R]):
        def wrapper(*args, **kwargs):
            nonlocal dictionary, new_capacity

            func_args = (args, tuple(kwargs.items()))

            if func_args in dictionary:
                value = dictionary.pop(func_args)
                dictionary[func_args] = value
                return value

            if len(dictionary) >= new_capacity:
                first_key, *_ = dictionary
                dictionary.pop(first_key)

            result = func(*args, **kwargs)
            dictionary[func_args] = result

            return result

        return wrapper

    return decorator


"""
@lru_cache(capacity=2)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")

    return greeting


print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
"""
"""
 dictionary = {}
    priority_list = []

    def decorator(func: Callable[P, R]):
        def wrapper(*args, **kwargs):
            nonlocal dictionary, priority_list, new_capacity

            func_args = (args, tuple(kwargs.items()))
            priority_list.append(func_args)

            if len(dictionary) == new_capacity:
                if func_args in dictionary:
                    priority_list.remove(func_args)
                    return dictionary[func_args]
                
                dictionary.pop(priority_list[0])
                priority_list.pop(0)
            
                result = func(*args, **kwargs)
                dictionary[func_args] = result
                return result
            
            if func_args in dictionary:
                    priority_list.remove(func_args)
                    return dictionary[func_args]
            
            result = func(*args, **kwargs)
            dictionary[func_args] = result
            return result   
            
        return wrapper
    return decorator
"""
"""
try:
        new_capacity = round(capacity)
    except Exception:
        raise TypeError from None
    else:
        if new_capacity < 1:      # < 1 или <= 1 ???
            raise ValueError from None
    
    dictionary = {}

    def decorator(func: Callable[P, R]):
        def wrapper(*args, **kwargs):
            nonlocal dictionary, new_capacity

            func_args = (args, tuple(kwargs.items()))
            
            if func_args in dictionary:
                return dictionary[func_args]
            
            if len(dictionary) >= new_capacity:
                dictionary.popitem(last = False)
            
            result = func(*args, **kwargs)
            dictionary[func_args] = result

            return result

            
        return wrapper
    return decorator
"""
