ALLOWED_TYPES = {"spotter_word", "voice_human", "voice_bot"}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    """
    Функция для валидации и агрегации данных разметки аудио сегментов.

    Args:
        segmentation_data: словарь, данные разметки аудиосегментов с полями:
            "audio_id" - уникальный идентификатор аудио.
            "segment_id" - уникальный идентификатор сегмента.
            "segment_start" - время начала сегмента.
            "segment_end" - время окончания сегмента.
            "type" - тип голоса в сегменте.

    Returns:
        Словарь с валидными сегментами, объединёнными по `audio_id`;
        Список `audio_id` (str), которые требуют переразметки.
    """
    result = {}
    need_to_remake = []
    checked_segments = {}

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")
        if not audio_id or not segment_id:
            continue

        if audio_id not in result:
            result[audio_id] = {}

        segment_key = (audio_id, segment_id)

        if segment_key in checked_segments:
            existing = checked_segments[segment_key]
            if (
                existing["start"] != segment["segment_start"]
                or existing["end"] != segment["segment_end"]
                or existing["type"] != segment["type"]
            ):
                need_to_remake.append(audio_id)
                if audio_id in result:
                    del result[audio_id]
            continue

        checked_segments[segment_key] = {
            "start": segment["segment_start"],
            "end": segment["segment_end"],
            "type": segment["type"],
        }

        segment_start, segment_end, segment_type = (
            segment["segment_start"],
            segment["segment_end"],
            segment["type"],
        )

        # Проверка на частично None значения
        segment_parts = [segment_type, segment_start, segment_end]
        none_count = sum(1 for part in segment_parts if part is None)

        if 0 < none_count < 3:
            need_to_remake.append(audio_id)
            if audio_id in result:
                del result[audio_id]
            continue

        if none_count == 3:
            # Все поля None - оставляем пустой словарь сегментов
            result[audio_id] = {}
            continue

        # Валидация типов и значений
        if (
            not isinstance(segment_type, str)
            or not isinstance(segment_start, (int, float))
            or not isinstance(segment_end, (int, float))
            or segment_type not in ALLOWED_TYPES
            or segment_start >= segment_end
        ):
            need_to_remake.append(audio_id)
            if audio_id in result:
                del result[audio_id]
            continue

        # Если все проверки пройдены - добавляем валидный сегмент
        result[audio_id][segment_id] = {
            "start": segment_start,
            "end": segment_end,
            "type": segment_type,
        }

    return result, need_to_remake
