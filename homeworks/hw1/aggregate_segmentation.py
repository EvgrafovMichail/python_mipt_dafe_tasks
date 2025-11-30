ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


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

    validated: dict[str, dict] = {}
    not_validated: set[str] = set()

    seen_segments: dict[
        tuple[str, str], tuple[float | None, float | None, str | None]
    ] = {}

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")
        s_start = segment.get("segment_start")
        s_end = segment.get("segment_end")
        s_type = segment.get("type")

        if audio_id is None:
            continue

        is_silent = s_type is None and s_start is None and s_end is None

        invalid = False

        if segment_id is None:
            invalid = True

        elif not is_silent:
            if not isinstance(s_type, str):
                invalid = True
            if not isinstance(s_start, float):
                invalid = True
            if not isinstance(s_end, float):
                invalid = True

        if not is_silent:
            if s_type is None or s_start is None or s_end is None:
                invalid = True

        if not is_silent and s_type not in ALLOWED_TYPES:
            invalid = True

        key = (audio_id, segment_id)
        if not is_silent:
            if key in seen_segments:
                prev = seen_segments[key]
                if prev != (s_start, s_end, s_type):
                    invalid = True
                    if audio_id in validated:
                        validated.pop(audio_id)
            else:
                seen_segments[key] = (s_start, s_end, s_type)

        if invalid:
            not_validated.add(audio_id)
            continue

        if audio_id not in validated:
            validated[audio_id] = {}

        if is_silent:

            validated.setdefault(audio_id, {})
            continue

        validated[audio_id][segment_id] = {
            "start": s_start,
            "end": s_end,
            "type": s_type,
        }

    return validated, list(not_validated)
