import pytest
import uuid
from unittest.mock import MagicMock, patch, Mock

from homeworks.hw1.aggregate_segmentation import aggregate_segmentation, ALLOWED_TYPES
from homeworks.hw1.backoff import backoff
from homeworks.hw1.cache import lru_cache
from homeworks.hw1.convert_exception import convert_exceptions_to_api_compitable_ones

NAME_BACKOFF_MODULE = "homeworks.hw1.backoff"


def test_valid_segments() -> None:
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


def test_empty_input() -> None:
    result_valid, result_forbidden = aggregate_segmentation([])
    assert result_valid == {}
    assert result_forbidden == []


def test_all_invalid_segments() -> None:
    input_data = [
        {
            "audio_id": "audio1",
            "segment_id": "seg1",
            "segment_start": 0.0,
            "segment_end": 1.0,
            "type": "invalid_type_1"
        },
    ]

    result_valid, result_forbidden = aggregate_segmentation(input_data)
    assert result_valid == {}
    assert result_forbidden == ["audio1"]


def test_duplicate_segment_ids() -> None:
    audio_id = str(uuid.uuid4())
    segment_id = str(uuid.uuid4())
    list_allow_types = list(ALLOWED_TYPES)

    input_data = [
        {
            "audio_id": audio_id,
            "segment_id": segment_id,
            "segment_start": 0.0,
            "segment_end": 1.0,
            "type": list_allow_types[0]
        },
    ]

    result_valid, result_forbidden = aggregate_segmentation(input_data)
    assert len(result_valid[audio_id]) == 1
    assert result_forbidden == []


def test_segment_with_none_values() -> None:
    audio_id = str(uuid.uuid4())
    segment_id = str(uuid.uuid4())

    input_data = [
        {
            "audio_id": audio_id,
            "segment_id": segment_id,
            "segment_start": None,
            "segment_end": None,
            "type": None
        },
    ]

    result_valid, result_forbidden = aggregate_segmentation(input_data)
    assert audio_id in result_valid
    assert result_valid[audio_id] == {}
    assert result_forbidden == []


def test_convert_matching_exception() -> None:
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


def test_convert_with_exception_instance() -> None:
    class ApiError(Exception):
        pass

    custom_error = ApiError("Кастомное сообщение")

    @convert_exceptions_to_api_compitable_ones({ValueError: custom_error})
    def func():
        raise ValueError("Внутренняя ошибка")

    with pytest.raises(ApiError) as exc_info:
        func()
    assert str(exc_info.value) == "Кастомное сообщение"


def test_no_exception_raised() -> None:
    class ApiError(Exception):
        pass

    @convert_exceptions_to_api_compitable_ones({ValueError: ApiError})
    def func():
        return "успех"

    result = func()
    assert result == "успех"


def test_multiple_exception_mappings() -> None:
    class ApiValueError(Exception):
        pass

    class ApiKeyError(Exception):
        pass

    @convert_exceptions_to_api_compitable_ones({
        ValueError: ApiValueError,
        KeyError: ApiKeyError
    })
    def func(exception_type):
        if exception_type == "value":
            raise ValueError("value error")
        elif exception_type == "key":
            raise KeyError("key error")
        else:
            raise RuntimeError("runtime error")

    with pytest.raises(ApiValueError):
        func("value")

    with pytest.raises(ApiKeyError):
        func("key")

    with pytest.raises(RuntimeError):
        func("runtime")


def test_exception_chaining_suppressed() -> None:
    class ApiError(Exception):
        pass

    @convert_exceptions_to_api_compitable_ones({ValueError: ApiError})
    def func():
        raise ValueError("оригинальная ошибка")

    try:
        func()
    except ApiError as e:
        assert e.__cause__ is None


@patch(NAME_BACKOFF_MODULE + '.sleep')
def test_exponential_backoff_and_jitter(mock_sleep: MagicMock) -> None:
    attempts = 0

    @backoff(
        retry_amount=3,
        timeout_start=0.1,
        timeout_max=1.0,
        backoff_scale=2.0
    )
    def func():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError("Ошибка подключения")
        return "успех"

    result = func()
    assert result == "успех"
    assert attempts == 3
    assert mock_sleep.call_count == 2


@patch(NAME_BACKOFF_MODULE + '.sleep')
def test_backoff_max_delay_respected(mock_sleep: MagicMock) -> None:
    @backoff(
        retry_amount=3,
        timeout_start=1.0,
        timeout_max=2.0,
        backoff_scale=3.0
    )
    def func():
        raise ConnectionError("Ошибка")

    with pytest.raises(ConnectionError):
        func()

    for call in mock_sleep.call_args_list:
        sleep_time = call[0][0]
        assert sleep_time <= 2.5


def test_success() -> None:
    capacity = 2
    call_args = [
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