from typing import Any

import pytest

# Импортируем тестируемую функцию и константу
from homeworks.hw1.aggregate_segmentation import ALLOWED_TYPES, aggregate_segmentation

# сюда тупа скопировать свой файл с 1 заданием
# и потом запустить счерез pytest


def test_aggregate_segmentation_with_invalid_type_after_valid_detailed():
    """Тест с дополнительными проверками состояния до и после невалидного сегмента"""
    segmentation_data = [
        {
            "audio_id": "audio_1",
            "segment_id": "segment_1",
            "segment_start": 0.0,
            "segment_end": 1.0,
            "type": "voice_human",
        },
        {
            "audio_id": "audio_2",  # Другой валидный audio_id
            "segment_id": "segment_3",
            "segment_start": 0.0,
            "segment_end": 1.0,
            "type": "voice_bot",
        },
        {
            "audio_id": "audio_1",  # Невалидный сегмент
            "segment_id": "segment_2",
            "segment_start": 1.0,
            "segment_end": 2.0,
            "type": "invalid_type",
        },
    ]

    valid_result, invalid_result = aggregate_segmentation(segmentation_data)

    # audio_1 должен быть в невалидных
    assert "audio_1" in invalid_result
    # audio_1 не должно быть в валидных
    assert "audio_1" not in valid_result
    # audio_2 должен остаться валидным
    assert "audio_2" in valid_result
    # В audio_2 должен быть один сегмент
    assert len(valid_result["audio_2"]) == 1
    # Проверяем содержимое сегмента audio_2
    assert valid_result["audio_2"]["segment_3"] == {"start": 0.0, "end": 1.0, "type": "voice_bot"}
