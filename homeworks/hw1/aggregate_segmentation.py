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
    valid_data: dict[str, dict[str, dict[str, str | float]]] = dict()
    audio_ids_re_marking: set[str] = set()

    temp_data: dict[str, dict[str, dict[str, str | float]]] = dict()

    for data in segmentation_data:
        audio_id = data.get("audio_id")
        segment_id = data.get("segment_id")
        segment_start = data.get("segment_start")
        segment_end = data.get("segment_end")
        voice_type = data.get("type")

        if not audio_id:
            continue

        if audio_id not in temp_data:
            temp_data[audio_id] = {}

        if not segment_id:
            audio_ids_re_marking.add(audio_id)
            continue

        all_none = all(val is None for val in (segment_start, segment_end, voice_type))

        if all_none:
            temp_data[audio_id][segment_id] = {
                "start": None,
                "end": None,
                "type": None,
            }
            continue

        some_none = any(val is None for val in (segment_start, segment_end, voice_type))

        if some_none:
            audio_ids_re_marking.add(audio_id)
            continue

        if not all(
            (
                isinstance(segment_start, float),
                isinstance(segment_end, float),
                isinstance(voice_type, str),
            )
        ):
            audio_ids_re_marking.add(audio_id)
            continue

        if voice_type not in ALLOWED_TYPES:
            audio_ids_re_marking.add(audio_id)
            continue

        if segment_id not in temp_data[audio_id]:
            temp_data[audio_id][segment_id] = {
                "start": segment_start,
                "end": segment_end,
                "type": voice_type,
            }
        else:
            start, end, v_type = temp_data[audio_id][segment_id].values()
            if (start, end, v_type) != (segment_start, segment_end, voice_type):
                audio_ids_re_marking.add(audio_id)

    for audio_id, segments_data in temp_data.items():
        if audio_id in audio_ids_re_marking:
            continue

        all_none = all(seg["type"] is None for seg in segments_data.values())

        if all_none:
            valid_data[audio_id] = {}
            continue

        valid_data[audio_id] = {
            seg_id: {
                "start": seg_data["start"],
                "end": seg_data["end"],
                "type": seg_data["type"],
            }
            for seg_id, seg_data in segments_data.items()
            if seg_data["type"] is not None
        }

    return (valid_data, list(audio_ids_re_marking))
