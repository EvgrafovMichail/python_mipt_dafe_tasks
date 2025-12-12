ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def is_segment_valid(segment: dict[str, str | float | None]) -> bool:
    """
    Функция для проверки валидности сегмента

    Args:
        segment: словарь, данные разметки аудиосегмента с полями:
            "audio_id" - уникальный идентификатор аудио.
            "segment_id" - уникальный идентификатор сегмента.
            "segment_start" - время начала сегмента.
            "segment_end" - время окончания сегмента.
            "type" - тип голоса в сегменте.

    Returns:
        True, если сегмент оказался валидным, иначе False
    """

    if not segment.get("segment_id"):
        return False

    are_fields_none = [segment.get(k) is None for k in ["type", "segment_start", "segment_end"]]
    if all(are_fields_none):
        return True

    if (
        not isinstance(segment.get("type"), str)
        or not isinstance(segment.get("segment_start"), float)
        or not isinstance(segment.get("segment_end"), float)
    ):
        return False

    if segment["type"] not in ALLOWED_TYPES:
        return False

    return True


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

    validated_data = {}
    invalid_data = set()

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        if not audio_id or (audio_id in invalid_data):
            continue

        validated_data.setdefault(audio_id, {})

        if not is_segment_valid(segment):
            invalid_data.add(audio_id)
            validated_data.pop(audio_id)
            continue

        if segment.get("type") is not None:  # if segment is not empty
            segment_id = segment["segment_id"]
            new_segment_data = {
                "start": segment["segment_start"],
                "end": segment["segment_end"],
                "type": segment["type"],
            }
            if (
                segment_id in validated_data[audio_id]
                and validated_data[audio_id][segment_id] != new_segment_data
            ):
                invalid_data.add(audio_id)
                validated_data.pop(audio_id)
                continue

            validated_data[audio_id][segment_id] = new_segment_data

    return validated_data, list(invalid_data)
