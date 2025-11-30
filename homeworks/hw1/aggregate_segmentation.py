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

    def _add_segment_data(seg_data, seg, val_data):
        if seg["audio_id"] in val_data:
            val_data[segment["audio_id"]][seg["segment_id"]] = seg_data
        else: 
            val_data[seg["audio_id"]] = {seg["segment_id"]: seg_data}

    valid_data = {}
    audio_ids_re_marking = set()

    for segment in segmentation_data:
        if ("segment_id" in segment and "audio_id" in segment):
            if (segment["audio_id"] not in valid_data
                or segment["audio_id"] in valid_data and segment["segment_id"] not in valid_data[segment["audio_id"]]):
                if (isinstance(segment["segment_start"], float)
                and isinstance(segment["segment_end"], float)
                and segment["type"] in ALLOWED_TYPES):
                    _add_segment_data({
                                    "segment_start": segment["segment_start"],
                                    "segment_end": segment["segment_end"],
                                    "type": segment["type"]
                                    },
                                    segment,
                                    valid_data)
                elif (segment["segment_start"] is None
                    and segment["segment_end"] is None
                    and segment["type"] is None):
                    _add_segment_data({},
                                    segment,
                                    valid_data)
                else:
                    audio_ids_re_marking.add(segment["audio_id"])
            elif ((segment["segment_start"] != valid_data[segment["audio_id"]][segment["segment_id"]]["segment_start"]
                       or segment["segment_end"] != valid_data[segment["audio_id"]][segment["segment_id"]]["segment_end"]
                       or segment["type"] != valid_data[segment["audio_id"]][segment["segment_id"]]["type"])):
                audio_ids_re_marking.add(segment["audio_id"])
                valid_data.pop([segment["audio_id"]])
        elif ("audio_id" in segment):
            audio_ids_re_marking.add(segment["audio_id"])

    return valid_data, list(audio_ids_re_marking)