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

    # ваш код
    audio_ids_re_marking = []  # черный список
    valid_data = {}  # белый список

    # проверочная функция

    def check(segment=dict, audio_id=str):
        segment_id = segment.get("segment_id")
        start = segment.get("segment_start")
        end = segment.get("segment_end")
        type_ = segment.get("type")

        if segment_id is None:
            return False

        if audio_id in valid_data:
            if segment_id in valid_data[audio_id]:
                return False

        if start is not None:
            if not isinstance(start, float):
                return False

        if end is not None:
            if not isinstance(end, float):
                return False

        if start is not None and end is not None:
            if end <= start:
                return False
            if start < 0 or end > 10:
                return False

        if type_ is not None:
            if type(type_) not in ALLOWED_TYPES:
                return False

        i = 0
        for x in [start, end, type_]:
            if x is None:
                i += 1
        if i not in [0, 3]:
            return False

        return True

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")

        if audio_id is None:
            continue
        if audio_id in audio_ids_re_marking:
            continue
        else:
            if check(segment, audio_id):
                segment_list = {
                    "start": segment.get("segment_start"),
                    "end": segment.get("segment_end"),
                    "type": segment.get("type"),
                }
                if audio_id in valid_data:
                    valid_data[audio_id][segment.get("segment_id")] = segment_list

                else:
                    valid_data[audio_id] = {segment.get("segment_id"): segment_list}

            else:
                if audio_id in valid_data:
                    del valid_data[audio_id]

                audio_ids_re_marking.append(audio_id)

    return valid_data, audio_ids_re_marking
