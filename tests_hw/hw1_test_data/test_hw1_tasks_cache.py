from unittest.mock import Mock

import pytest

# Импортируем тестируемую функцию
from homeworks.hw1.cache import lru_cache

"""

    Списки с аргументами:
 
        * первый параметр - количество аргументов
        * второй параметр - возможные типы
        * третий параметр - повторение аргументов
        * четвертый параметр - размер

"""

ARGS_DICT: dict[str, list[tuple[object]]] = {
    
    'one_int_without_repeating_args_small': [
        (2), 
        (1),
    ],

    'one_int_with_repeating_args_small': [
        (2), 
        (1), 
        (2), 
        (1), 
        (1),
    ],

    'one_int_with_repeating_args_huge': [
        (1), #c
        (2), #c
        (2),
        (1),
        (2),
        (1),
        (1),
        (2),
        (1),
        (1),
        (3), #c
        (1), 
        (1),
        (3),
        (2), #c
        (1), #c
        (1),
        (1),
        (1),
        (3), #c
        (1),
        (3),
        (2), #c
        (1), #c
        (3), #c
        (2), #c
        (1), #c
        (1),
    ],

    'three_str_with_repeating_args_small': [
        ('first', 'second', 'third'), #1 o
        ('first', 'third', 'second'), #2 o
        ('third', 'first', 'third'), #3 o
        ('first', 'second', 'third'), #1 o
        ('first', 'third', 'second'), #2 o
        ('first', 'second', 'first'), #4 o
        ('third', 'first', 'third'), #3 o
        ('first', 'second', 'third'), #1 o
    ],

    'two_multi_with_repeating_args_small': [
        (42, 'str'), #o #o
        (5.6, TypeError), #o #o
        (7 + 7j, None), #o #o
        (5.6, TypeError),
        (7 + 7j, None),
        (5.6, TypeError),
        (42, 'str'), #o
        (5.6, TypeError),
        (True, False), #o #o
        (42, 'str'), #o
        (7 + 7j, None), #o #o
        (True, False), #o
        (5.6, TypeError), #o #o
        (42, 'str'), #o #o
        (42, 'str'),
        (7 + 7j, None), #o #o
        (7 + 7j, None),
        (42, 'str'),
        (True, False), #o #o
    ]
}

"""Тесты для декоратора LRU-cache"""

@pytest.mark.parametrize("capacity, call_count_expected, call_args", [
    (2, 2, ARGS_DICT['one_int_without_repeating_args_small']),
    (2, 2, ARGS_DICT['one_int_with_repeating_args_small']),
    (2, 11, ARGS_DICT['one_int_with_repeating_args_huge']),
    (2, 8, ARGS_DICT['three_str_with_repeating_args_small']),
    (2, 12, ARGS_DICT['two_multi_with_repeating_args_small']),
    (5, 3, ARGS_DICT['one_int_with_repeating_args_huge']),
    (3, 6, ARGS_DICT['three_str_with_repeating_args_small']),
    (3, 9, ARGS_DICT['two_multi_with_repeating_args_small']),
])

def test_cache(
    capacity: int, 
    call_count_expected: int, 
    call_args: list[tuple[object]]
) -> None:
    
    mock_func = Mock()
    func_cached = lru_cache(capacity=capacity)(mock_func)

    for args in call_args:
        func_cached(args)

    assert mock_func.call_count == call_count_expected

def test_exception_value_error(
) -> None:
    
    capacity: float = 0.4
    mock_func = Mock()
    with pytest.raises(ValueError):
        lru_cache(capacity=capacity)(mock_func)

def test_exception_type_error(
) -> None:
    
    capacity = None
    mock_func = Mock()
    with pytest.raises(TypeError):
        lru_cache(capacity=capacity)(mock_func)