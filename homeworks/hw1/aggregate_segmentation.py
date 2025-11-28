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

    valid_segments = {}
    need_remark = set()

    audio_groups = {}
    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        if audio_id is None:
            continue

        if audio_id not in audio_groups:
            audio_groups[audio_id] = []
        audio_groups[audio_id].append(segment)

    for audio_id, segments in audio_groups.items():
        segment_dict = {}
        segment_ids_seen = {}
        audio_has_invalid = False

        speech_segments = {}
        speechless_segments = set()

        for segment in segments:
            try:
                segment_id = segment.get("segment_id")

                if segment_id is None:
                    audio_has_invalid = True
                    continue

                type_val = segment.get("type")
                start_val = segment.get("segment_start")
                end_val = segment.get("segment_end")

                if not isinstance(type_val, (str, type(None))):
                    audio_has_invalid = True
                    continue
                if not isinstance(start_val, (float, type(None))):
                    audio_has_invalid = True
                    continue
                if not isinstance(end_val, (float, type(None))):
                    audio_has_invalid = True
                    continue

                none_count = [type_val, start_val, end_val].count(None)
                if none_count > 0 and none_count < 3:
                    audio_has_invalid = True
                    continue

                if none_count == 3:
                    speechless_segments.add(segment_id)
                    continue

                if type_val not in ALLOWED_TYPES:
                    audio_has_invalid = True
                    continue

                if segment_id in segment_ids_seen:
                    existing = segment_ids_seen[segment_id]
                    if (
                        existing["start"] != start_val
                        or existing["end"] != end_val
                        or existing["type"] != type_val
                    ):
                        audio_has_invalid = True
                        continue
                else:
                    segment_ids_seen[segment_id] = {
                        "start": start_val,
                        "end": end_val,
                        "type": type_val,
                    }

                speech_segments[segment_id] = {"start": start_val, "end": end_val, "type": type_val}

            except Exception:
                audio_has_invalid = True
                continue

        for segment_id, segment_data in speech_segments.items():
            segment_dict[segment_id] = segment_data
        if audio_has_invalid:
            need_remark.add(audio_id)
        else:
            valid_segments[audio_id] = segment_dict

    return valid_segments, list(need_remark)
