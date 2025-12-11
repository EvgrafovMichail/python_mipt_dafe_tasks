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
    invalid_result = set()

    for current in segmentation_data:
        audio_id = current["audio_id"]
        segment_id = current["segment_id"]
        segment_start = current["segment_start"]
        segment_end = current["segment_end"]
        # type - bad name for a variable
        # so i use prefics "current"
        current_type = current["type"]

        if not audio_id:
            continue
        if audio_id in invalid_result:
            continue

        # check for none value
        none_flag = (current_type is None) == (segment_start is None) == (segment_end is None)

        # check for type conformity
        if (current_type is None) and (segment_start is None) and (segment_end is None):
            type_flag = True
        else:
            type_flag = (
                isinstance(current_type, str)
                and isinstance(segment_start, float)
                and isinstance(segment_end, float)
            )

        if not (
            segment_id
            and none_flag
            and type_flag
            and (current_type in ALLOWED_TYPES or current_type is None)
        ):
            invalid_result.add(audio_id)
            valid_result.pop(audio_id, None)
            continue

        else:
            if audio_id not in valid_result:
                valid_result[audio_id] = {}

            else:
                local_audio = valid_result[audio_id]
                if segment_id in local_audio:
                    if (
                        (local_audio[segment_id]["start"] != segment_start)
                        or (local_audio[segment_id]["end"] != segment_end)
                        or (local_audio[segment_id]["type"] != current_type)
                    ):
                        invalid_result.add(audio_id)
                        valid_result.pop(audio_id, None)
                        continue
                    else:
                        continue
            if (current_type is None) and (segment_start is None) and (segment_end is None):
                continue
            result = {
                "start": segment_start,
                "end": segment_end,
                "type": current_type,
            }
            valid_result[audio_id][segment_id] = result

    return valid_result, list(invalid_result)
