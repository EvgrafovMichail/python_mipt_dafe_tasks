ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def is_valid_segment(audio_segment):
    segment_id = audio_segment.get("segment_id")
    type_val = audio_segment.get("type")
    start_val = audio_segment.get("segment_start")
    end_val = audio_segment.get("segment_end")

    if segment_id is None:
        return False

    if type_val is None and start_val is None and end_val is None:
        return True

    if not (
        isinstance(type_val, str) and isinstance(
            start_val, float) and isinstance(end_val, float)
    ):
        return False

    if type_val not in ALLOWED_TYPES:
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

    result_dict = {}
    wrong_audio = set()
    segment_info = {}

    for audio_segment in segmentation_data:
        audio_id = audio_segment.get("audio_id")
        segment_id = audio_segment.get("segment_id")

        if audio_id is None:
            continue

        if not is_valid_segment(audio_segment):
            wrong_audio.add(audio_id)
            continue

        key = (audio_id, segment_id)

        curr_val = (
            audio_segment.get("segment_start"),
            audio_segment.get("segment_end"),
            audio_segment.get("type"),
        )

        if key in segment_info:
            if segment_info[key] != curr_val:
                wrong_audio.add(audio_id)
        else:
            segment_info[key] = curr_val

    for audio_segment in segmentation_data:
        audio_id = audio_segment.get("audio_id")
        segment_id = audio_segment.get("segment_id")
        type_val = audio_segment.get("type")
        start_val = audio_segment.get("segment_start")
        end_val = audio_segment.get("segment_end")

        if audio_id is None:
            continue
        if audio_id in wrong_audio:
            continue

        if audio_id not in result_dict:
            result_dict[audio_id] = {}

        if type_val is None and start_val is None and end_val is None:
            continue

        result_dict[audio_id][segment_id] = {
            "type": type_val, "start": start_val, "end": end_val}
    return result_dict, list(wrong_audio)
