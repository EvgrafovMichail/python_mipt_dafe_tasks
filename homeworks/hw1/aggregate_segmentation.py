ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}

def valid_check(segment: dict):
    segment_start = segment.get("segment_start")
    segment_end = segment.get("segment_end")
    segment_type = segment.get("segment_type")

    if segment_start is not None and not isinstance(segment_start, float):
        return False
    if segment_end is not None and not isinstance(segment_end, float):
        return False
    if segment_type is not None and not isinstance(segment_type, str):
        return False
    

    none_count = sum(1 for field in [segment_start, segment_end, segment_type] if field is None)


    if none_count not in [0,3]:
        return False
    

    if none_count == 3:
        return True

    
    if segment_type not in ALLOWED_TYPES:
        return False

    
    if segment_start >= segment_end:
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

    valid_data = {}
    audio_ids_re_marking_set = set()
    segment_unique = {}
    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")

        if audio_id is None:
            continue


        if segment_id is None:
            audio_ids_re_marking_set.add(audio_id)
            continue

        key = (audio_id, segment_id)

        if key in segment_unique:
            check_segment = segment_unique[key]
            if (check_segment["segment_start"] != segment["segment_start"] or check_segment["segment_end"] != segment["segment_end"] or check_segment["type"] != segment["type"]):
                audio_ids_re_marking_set.add(audio_id)
            continue
        else:
            segment_unique[key] = segment
        
        if not valid_check(segment):
            audio_ids_re_marking_set.add(audio_id)
            continue


        if audio_id not in valid_data:
            valid_data[audio_id] = {}


        if segment["segment_start"] is None and segment["segment_end"] is None and segment["type"] is None:
            continue
        else:
            valid_data[audio_id][segment_id] = {
                "start": segment["segment_start"],
                "end": segment["segment_end"],
                "type": segment["type"]
            }
        

    for audio_id in audio_ids_re_marking_set:
        if audio_id in valid_data:
            del valid_data[audio_id]

    
    return valid_data, list(audio_ids_re_marking_set)