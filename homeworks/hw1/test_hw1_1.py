import pytest
from typing import Any

# Импортируем тестируемую функцию и константу
from homeworks.hw1.aggregate_segmentation import aggregate_segmentation, ALLOWED_TYPES


class TestAggregateSegmentation:
    """Тесты для функции агрегации сегментации аудио данных."""

    def test_valid_segments_different_audio_ids(self):
        """Тест валидных сегментов с разными audio_id."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-456",
                "segment_id": "seg-2",
                "segment_start": 1.0,
                "segment_end": 3.0,
                "type": "voice_bot",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert "audio-123" in valid
        assert "audio-456" in valid
        assert valid["audio-123"]["seg-1"]["type"] == "voice_human"
        assert valid["audio-456"]["seg-2"]["type"] == "voice_bot"

    def test_valid_segments_same_audio_id(self):
        """Тест валидных сегментов с одинаковым audio_id."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-2",
                "segment_start": 3.0,
                "segment_end": 5.0,
                "type": "spotter_word",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert len(valid["audio-123"]) == 2
        assert "seg-1" in valid["audio-123"]
        assert "seg-2" in valid["audio-123"]

    def test_segments_without_voice_all_none(self):
        """Тест сегментов без голоса (все поля None) - должен создать пустой словарь."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": None,
                "segment_end": None,
                "type": None,
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-2",
                "segment_start": None,
                "segment_end": None,
                "type": None,
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert valid["audio-123"] == {}

    def test_mixed_voice_and_no_voice_segments(self):
        """Тест смешанных сегментов (с голосом и без) для одного audio_id."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-2",
                "segment_start": None,
                "segment_end": None,
                "type": None,
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert len(valid["audio-123"]) == 1  # Только сегмент с голосом
        assert "seg-1" in valid["audio-123"]
        assert "seg-2" not in valid["audio-123"]

    def test_duplicate_segments_same_data(self):
        """Тест дубликатов сегментов с одинаковыми данными (должны игнорироваться)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert len(valid["audio-123"]) == 1

    def test_missing_segment_id(self):
        """Тест отсутствующего segment_id."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "",  # Пустой ID
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-2",
                "segment_start": 1.0,
                "segment_end": 3.0,
                "type": "voice_bot",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        assert len(valid.get("audio-123", {})) == 0

    @pytest.mark.parametrize(
        "field,value",
        [
            ("type", 123),  # type не строка
            ("segment_start", "not_float"),  # start не float
            ("segment_end", "not_float"),  # end не float
        ],
    )
    def test_invalid_field_types(self, field: str, value: Any):
        """Тест невалидных типов полей."""
        base_segment = {
            "audio_id": "audio-123",
            "segment_id": "seg-1",
            "segment_start": 0.5,
            "segment_end": 2.5,
            "type": "voice_human",
        }
        base_segment[field] = value
        data = [base_segment]

        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        assert len(valid) == 0

    @pytest.mark.parametrize(
        "segment_start,segment_end,type_val",
        [
            (None, 2.5, "voice_human"),  # Только start None
            (0.5, None, "voice_human"),  # Только end None
            (0.5, 2.5, None),  # Только type None
            (None, None, "voice_human"),  # Только type не None
            (0.5, None, None),  # Только start не None
        ],
    )
    def test_partial_none_values(self, segment_start: Any, segment_end: Any, type_val: Any):
        """Тест частичных None значений (должны быть невалидными)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": segment_start,
                "segment_end": segment_end,
                "type": type_val,
            }
        ]
        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        assert len(valid) == 0

    def test_type_not_in_allowed_types(self):
        """Тест type не из ALLOWED_TYPES."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "invalid_type",
            }
        ]
        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        assert len(valid) == 0

    def test_duplicate_segments_different_data(self):
        """Тест дубликатов сегментов с разными данными (должно быть невалидно)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 1.0,  # Другой start
                "segment_end": 3.0,
                "type": "voice_human",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        # Проверяем, что валидные сегменты не добавлены
        assert len(valid.get("audio-123", {})) == 0

    def test_missing_audio_id(self):
        """Тест отсутствующего audio_id (должен игнорироваться)."""
        data = [
            {
                "audio_id": "",  # Пустой ID
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-2",
                "segment_start": 1.0,
                "segment_end": 3.0,
                "type": "voice_bot",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert "audio-123" in valid
        assert len(valid["audio-123"]) == 1

    def test_empty_input(self):
        """Тест пустого входного списка."""
        valid, invalid = aggregate_segmentation([])

        assert len(valid) == 0
        assert len(invalid) == 0

    def test_audio_id_with_mixed_valid_invalid_segments(self):
        """Тест audio_id с валидными и невалидными сегментами (весь audio_id невалиден)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "",  # Невалидный сегмент
                "segment_start": 1.0,
                "segment_end": 3.0,
                "type": "voice_bot",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        assert len(valid) == 0

    def test_multiple_invalid_segments_same_audio_id(self):
        """Тест нескольких невалидных сегментов для одного audio_id (в списке должен быть один раз)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "",  # Невалидный
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": "voice_human",
            },
            {
                "audio_id": "audio-123",
                "segment_id": "seg-2",
                "segment_start": None,  # Невалидный (частичный None)
                "segment_end": 3.0,
                "type": "voice_bot",
            },
            {
                "audio_id": "audio-456",
                "segment_id": "seg-3",
                "segment_start": 1.0,
                "segment_end": 2.0,
                "type": "voice_human",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert "audio-123" in invalid
        assert "audio-456" not in invalid
        assert invalid.count("audio-123") == 1  # Только один раз
        assert len(valid) == 1
        assert "audio-456" in valid

    def test_time_validation_edge_cases(self):
        """Тест краевых случаев времени."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 0.0,  # Ноль
                "segment_end": 10.0,  # Максимум
                "type": "voice_human",
            },
            {
                "audio_id": "audio-456",
                "segment_id": "seg-2",
                "segment_start": 5.0,
                "segment_end": 5.0,  # Нулевая длительность
                "type": "spotter_word",
            },
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert len(valid) == 2

    @pytest.mark.performance
    def test_large_dataset(self):
        """Производственный тест на большом наборе данных."""
        data = []
        # 100 разных audio_id, каждый с 10 сегментами
        for i in range(100):
            audio_id = f"audio-{i}"
            for j in range(10):
                data.append(
                    {
                        "audio_id": audio_id,
                        "segment_id": f"seg-{i}-{j}",
                        "segment_start": float(j),
                        "segment_end": float(j + 1),
                        "type": "voice_human" if j % 2 == 0 else "voice_bot",
                    }
                )

        valid, invalid = aggregate_segmentation(data)

        assert len(valid) == 100
        assert len(invalid) == 0
        assert all(len(segments) == 10 for segments in valid.values())

    def test_mixed_allowed_types(self):
        """Тест всех разрешенных типов."""
        data = [
            {
                "audio_id": f"audio-{i}",
                "segment_id": f"seg-{i}",
                "segment_start": 0.5,
                "segment_end": 2.5,
                "type": voice_type,
            }
            for i, voice_type in enumerate(ALLOWED_TYPES)
        ]
        valid, invalid = aggregate_segmentation(data)

        assert len(invalid) == 0
        assert len(valid) == len(ALLOWED_TYPES)

    def test_negative_time_values(self):
        """Тест отрицательных значений времени (должны быть валидны, так как не проверяются)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": -1.0,
                "segment_end": -0.5,
                "type": "voice_human",
            }
        ]
        valid, invalid = aggregate_segmentation(data)

        # В текущей реализации это считается валидным
        assert "audio-123" not in invalid
        assert "audio-123" in valid

    def test_start_greater_than_end(self):
        """Тест когда start > end (должно быть валидно, так как не проверяется)."""
        data = [
            {
                "audio_id": "audio-123",
                "segment_id": "seg-1",
                "segment_start": 5.0,
                "segment_end": 2.0,
                "type": "voice_human",
            }
        ]
        valid, invalid = aggregate_segmentation(data)

        # В текущей реализации это считается валидным
        assert "audio-123" not in invalid
        assert "audio-123" in valid
        assert valid["audio-123"]["seg-1"]["start"] == 5.0
        assert valid["audio-123"]["seg-1"]["end"] == 2.0
