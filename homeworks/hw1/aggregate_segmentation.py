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

    valid_result = {}
    audio_invalid = set()
    seen_segments = {}
    audio_has_any_segment = set()

    def vailid_segment(segment):
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")
        typ = segment.get("type")
        start = segment.get("segment_start")
        end = segment.get("segment_end")

        if audio_id is None:
            return False

        if segment_id is None:
            return False

        if typ is None and start is None and end is None:
            return True

        if typ is None or start is None or end is None:
            return False

        if not isinstance(typ, str):
            return False

        if not (isinstance(start, float) and isinstance(end, float)):
            return False

        if typ not in ALLOWED_TYPES:
            return False

        if start >= end:
            return False

        return True

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")
        typ = segment.get("type")
        start = segment.get("segment_start")
        end = segment.get("segment_end")

        if audio_id is None:
            continue

        audio_has_any_segment.add(audio_id)

        if not vailid_segment(segment):
            audio_invalid.add(audio_id)
            continue

        key = (audio_id, segment_id)

        if key in seen_segments:
            data = seen_segments[key]
            if data != (typ, start, end):
                audio_invalid.add(audio_id)
                continue
        else:
            seen_segments[key] = (typ, start, end)

        if not (typ is None and start is None and end is None):
            if audio_id not in valid_result:
                valid_result[audio_id] = {}
            valid_result[audio_id][segment_id] = {
                "type": typ,
                "start": start,
                "end": end,
            }

    for audio_id in audio_has_any_segment:
        if audio_id not in audio_invalid and audio_id not in valid_result:
            valid_result[audio_id] = {}

    for bad in audio_invalid:
        if bad in valid_result:
            del valid_result[bad]

    return valid_result, sorted(audio_invalid)
