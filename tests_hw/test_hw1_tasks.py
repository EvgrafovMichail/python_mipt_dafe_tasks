import pytest
import uuid
from unittest.mock import MagicMock, patch, Mock

from homeworks.hw1.aggregate_segmentation import aggregate_segmentation, ALLOWED_TYPES

from homeworks.hw1.backoff import backoff
from homeworks.hw1.cache import lru_cache

from homeworks.hw1.convert_exception import convert_exceptions_to_api_compitable_ones


from tests_hw.hw1_test_data.cache_test_data import (
    TESTCASE_DATA,
    TESTCASE_IDS,
)


NAME_BACKOFF_MODULE = "homeworks.hw1.backoff" # название модуля с backoff

def test_valid_segments() -> None:
    """Тест: валидные сегменты."""
    list_allow_types = list(ALLOWED_TYPES)
    audio_id_1 = str(uuid.uuid4())
    audio_id_2 = str(uuid.uuid4())
    audio_id_3 = str(uuid.uuid4())

    segment_id_1 = str(uuid.uuid4())
    segment_id_2 = str(uuid.uuid4())
    segment_id_3 = str(uuid.uuid4())
    segment_id_4 = str(uuid.uuid4())
    segment_id_5 = str(uuid.uuid4())

    input_data = [
        {
            "audio_id": audio_id_1,
            "segment_id": segment_id_1,
            "segment_start": 0.0,
            "segment_end": 1.0,
            "type": list_allow_types[0]
        },
        {
            "audio_id": audio_id_1,
            "segment_id": segment_id_2,
            "segment_start": 2.5,
            "segment_end": 3.5,
            "type": list_allow_types[1]
        },
        {
            "audio_id": audio_id_2,
            "segment_id": segment_id_3,
            "segment_start": 4.5,
            "segment_end": 4.6,
            "type": list_allow_types[0]
        },
        {
            "audio_id": audio_id_2,
            "segment_id": segment_id_4,
            "segment_start": 5.5,
            "segment_end": 6.5,
            "type": list_allow_types[1]
        },
        {
            "audio_id": audio_id_3,
            "segment_id": segment_id_5,
            "segment_start": None,
            "segment_end": None,
            "type": None
        },
        {
            "audio_id": "audio3",
            "segment_id": "seg5",
            "segment_start": 0.0,
            "segment_end": 1.0,
            "type": "invalid_type"
        },
    ]

    expected_valid = {
        audio_id_1: {
            segment_id_1: {"start": 0.0, "end": 1.0, "type": list_allow_types[0]},
            segment_id_2: {"start": 2.5, "end": 3.5, "type": list_allow_types[1]}
        },
        audio_id_2: {
            segment_id_3: {"start": 4.5, "end": 4.6, "type": list_allow_types[0]},
            segment_id_4: {"start": 5.5, "end": 6.5, "type": list_allow_types[1]}
        },
        audio_id_3: {},
    }
    expected_forbidden = ["audio3"]

    result_valid, result_forbidden = aggregate_segmentation(input_data)
    assert result_valid == expected_valid
    assert result_forbidden == expected_forbidden


def test_convert_matching_exception() -> None:
    """Тест: исключение заменяется на API-совместимое."""

    class ApiValueError(Exception):
        pass

    @convert_exceptions_to_api_compitable_ones({ValueError: ApiValueError})
    def func():
        raise ValueError("Внутренняя ошибка")
    
    @convert_exceptions_to_api_compitable_ones({ValueError: ApiValueError})
    def func2():
        raise KeyError("Внутренняя ошибка")

    with pytest.raises(ApiValueError):
        func()

    with pytest.raises(KeyError):
        func2()

@patch(NAME_BACKOFF_MODULE + '.sleep')
def test_exponential_backoff_and_jitter(mock_sleep: MagicMock) -> None:
    """Тест: задержки увеличиваются, но не выше timeout_max и к ним добавляется дрожь."""
    attempts = 0
    timeout_max = 4
    retry_amount = 4
    timeouts = [1, 2, 4, 4]

    @backoff(
        retry_amount=retry_amount,
        timeout_start=1,
        timeout_max=timeout_max,
        backoff_scale=2.0
    )
    def func():
        nonlocal attempts
        attempts += 1
        if attempts < retry_amount:
            raise ConnectionError("Ошибка подключения")
        return "успех"

    result = func()
    assert result == "успех"
    assert mock_sleep.call_count == retry_amount - 1

    count_more_av_time = 0
    args_list = map(lambda call_val: call_val.args[0], mock_sleep.call_args_list)
    for av_time, args in zip(timeouts, args_list):
        count_more_av_time += args > av_time
        assert av_time <= args <= av_time + 0.5
    
    assert count_more_av_time   # есть добавление "дрожи"

def test_success() -> None:
    capacity = 2
    call_args =  [
        (1, 2),
        (1, 2),
        (2, 2),
    ]
    call_count_expected = 2
    
    mock_func = Mock()
    func_cached = lru_cache(capacity=capacity)(mock_func)

    for args in call_args:
        func_cached(args)

    assert mock_func.call_count == call_count_expected
