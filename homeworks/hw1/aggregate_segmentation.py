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
    valid_data, ids_re_marking = {}, []
    for segment in segmentation_data:
        if segment["audio_id"] in ids_re_marking:
            continue

        if "segment_id" not in segment:
            ids_re_marking.append(segment["audio_id"])
            continue

        audio_id = segment["audio_id"]
        segment_id = segment["segment_id"]
        start = segment["segment_start"]
        end = segment["segment_end"]
        segment_type = segment["type"]

        if is_all_none(lst := [start, end, segment_type]):
            valid_data[audio_id] = {}
            continue

        if not is_valid_type(segment_type) or is_any_none(lst):
            ids_re_marking.append(audio_id)
            continue

        if not (isinstance(start, float) and isinstance(end, float)):
            ids_re_marking.append(audio_id)
            continue

        if audio_id not in valid_data:
            valid_data[audio_id] = {}

        if audio_id in valid_data:
            segment_dict = dict()
            segment_dict[segment_id] = {
                "start": start,
                "end": end,
                "type": segment_type,
            }
            if segment_id not in valid_data[audio_id]:
                valid_data[audio_id].update(segment_dict)
            else:
                old_start = valid_data[audio_id][segment_id]["start"]
                old_end = valid_data[audio_id][segment_id]["end"]
                old_type = valid_data[audio_id][segment_id]["type"]
                if not (old_start == start and old_end == end and old_type == segment_type):
                    ids_re_marking.append(audio_id)
                    valid_data.pop(audio_id)
    return valid_data, ids_re_marking


def is_valid_type(_type) -> bool:
    return _type is None or _type in ALLOWED_TYPES


def is_all_none(lst: list) -> bool:
    return all([x is None for x in lst])


def is_any_none(lst: list) -> bool:
    return any([x is None for x in lst])
