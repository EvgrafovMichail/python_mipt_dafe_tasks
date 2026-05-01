ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}
"""Тест: валидные сегменты."""
list_allow_types = list(ALLOWED_TYPES)
audio_id_1 = str(1)
audio_id_2 = str(2)
audio_id_3 = str(3)

segment_id_1 = str(1)
segment_id_2 = str(2)
segment_id_3 = str(3)
segment_id_4 = str(4)
segment_id_5 = str(5)

input_data = [
    {
        "audio_id": audio_id_1,
        "segment_id": segment_id_1,
        "segment_start": 0.0,
        "segment_end": 1.0,
        "type": list_allow_types[0],
    },
    {
        "audio_id": audio_id_1,
        "segment_id": segment_id_2,
        "segment_start": 2.5,
        "segment_end": 3.5,
        "type": list_allow_types[1],
    },
    {
        "audio_id": audio_id_2,
        "segment_id": segment_id_3,
        "segment_start": 4.5,
        "segment_end": 4.6,
        "type": list_allow_types[0],
    },
    {
        "audio_id": audio_id_2,
        "segment_id": segment_id_4,
        "segment_start": 5.5,
        "segment_end": 6.5,
        "type": list_allow_types[1],
    },
    {
        "audio_id": audio_id_3,
        "segment_id": segment_id_5,
        "segment_start": None,
        "segment_end": None,
        "type": None,
    },
    {
        "audio_id": "audio3",
        "segment_id": "seg5",
        "segment_start": 0.0,
        "segment_end": 1.0,
        "type": "invalid_type",
    },
]


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
    audio_ids_with_empty_segs = set()

    for segment in segmentation_data:
        segment_id = segment.get("segment_id")
        audio_id = segment.get("audio_id")
        start = segment.get("segment_start")
        end = segment.get("segment_end")
        type = segment.get("type")

        if segment_id and audio_id:
            if (
                audio_id not in valid_data
                or audio_id in valid_data
                and segment_id not in valid_data[audio_id]
            ):
                if isinstance(start, float) and isinstance(end, float) and type in ALLOWED_TYPES:
                    _add_segment_data(
                        {"start": start, "end": end, "type": type}, segment, valid_data
                    )

                elif start is None and end is None and type is None:
                    _add_segment_data({}, segment, valid_data)
                    audio_ids_with_empty_segs.add(audio_id)

                else:
                    audio_ids_re_marking.add(audio_id)
                    if audio_id in valid_data:
                        valid_data.pop(audio_id)

            elif (
                start != valid_data[audio_id][segment_id][start]
                or end != valid_data[audio_id][segment_id][end]
                or type != valid_data[audio_id][segment_id][type]
            ):
                audio_ids_re_marking.add(audio_id)
                valid_data.pop(audio_id)

        elif audio_id:
            audio_ids_re_marking.add(audio_id)
            if audio_id in valid_data:
                valid_data.pop(audio_id)

    for id in audio_ids_with_empty_segs:
        if all(val == {} for val in valid_data[id].values()):
            valid_data[id] = {}

    return valid_data, list(audio_ids_re_marking)


print(aggregate_segmentation(input_data))
