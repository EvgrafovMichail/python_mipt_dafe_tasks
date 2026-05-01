ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def is_segment_valid(
    audio_id: str | None,
    segment_id: str | None,
    segment_type: str | None,
    segment_start: float | None,
    segment_end: float | None,
) -> bool:
    """
    Проверяет валидность сегмента.
    Возвращает True если сегмент валиден, False если невалиден.
    """

    if audio_id is None or segment_id is None:
        return False

    if segment_type is not None and not isinstance(segment_type, str):
        return False
    if segment_start is not None and not isinstance(segment_start, (int, float)):
        return False
    if segment_end is not None and not isinstance(segment_end, (int, float)):
        return False

    all_none = segment_type is None and segment_start is None and segment_end is None
    if all_none:
        return True

    any_none = segment_type is None or segment_start is None or segment_end is None
    if any_none:
        return False

    if segment_type not in ALLOWED_TYPES:
        return False

    return True


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data = {}
    audio_ids_re_marking = []

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")
        segment_type = segment.get("type")
        segment_start = segment.get("segment_start")
        segment_end = segment.get("segment_end")

        if audio_id is None or audio_id in audio_ids_re_marking:
            continue

        is_valid = is_segment_valid(audio_id, segment_id, segment_type, segment_start, segment_end)

        if not is_valid:
            audio_ids_re_marking.append(audio_id)
            if audio_id in valid_data:
                del valid_data[audio_id]
            continue

        if segment_end is None and segment_start is None and segment_type is None:
            if audio_id not in valid_data:
                valid_data[audio_id] = {}
            continue

        if audio_id in valid_data and segment_id in valid_data[audio_id]:
            existing_segment = valid_data[audio_id][segment_id]
            if (
                existing_segment["type"] != segment_type
                or existing_segment["start"] != segment_start
                or existing_segment["end"] != segment_end
            ):
                audio_ids_re_marking.append(audio_id)
                del valid_data[audio_id]
                continue

        if audio_id not in valid_data:
            valid_data[audio_id] = {}

        valid_data[audio_id][segment_id] = {
            "type": segment_type,
            "start": segment_start,
            "end": segment_end,
        }

    return valid_data, audio_ids_re_marking
