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
    need_remark = set()
    right_data = {}
    for segment in segmentation_data:
        audio_id = segment["audio_id"]
        segment_id = segment["segment_id"]
        segment_start = segment["segment_start"]
        segment_end = segment["segment_end"]
        type = segment["type"]
        if audio_id is not None:
            if segment_id is None:
                need_remark.add(audio_id)
            elif segment_end is None and segment_start is None and type is None:
                if not (audio_id in right_data):
                    right_data[audio_id] = {}
                continue
            elif not isinstance(segment_start, float):
                need_remark.add(audio_id)
            elif not isinstance(segment_end, float):
                need_remark.add(audio_id)
            elif not isinstance(type, str):
                need_remark.add(audio_id)
            elif not (type in ALLOWED_TYPES):
                need_remark.add(audio_id)
            elif segment_end is None or segment_start is None or type is None:
                need_remark.add(audio_id)
            else:
                if audio_id in right_data and segment_id in right_data[audio_id]:
                    another_data = right_data[audio_id][segment_id]
                    if (
                        another_data["type"] != type
                        or another_data["segment_end"] != segment_end
                        or another_data["segment_start"] != segment_start
                    ):
                        need_remark.add(audio_id)
                        right_data.pop([audio_id][segment_id])
                else:
                    if audio_id not in right_data:
                        right_data[audio_id] = {}
                    right_data[audio_id][segment_id] = {
                        "type": type,
                        "segment_start": segment_start,
                        "segment_end": segment_end,
                    }
    return right_data, list(need_remark)
