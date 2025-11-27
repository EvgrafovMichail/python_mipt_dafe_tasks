ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}
def validate_segment( audio_id, segment_id,segment_type,segment_start,segment_end) -> bool:
    if segment_id is None:
        return False
    # все None
    if segment_start is None and segment_end is None and segment_type is None:
        return True
    
    # проверка типов данных
    if not isinstance(segment_type, str):
        return False
    
    if not isinstance(segment_start,  float):
        return False
    
    if not isinstance(segment_end, float):
        return False
    
    #не все None, но некоторые None
    if segment_start is None or segment_end is None or segment_type is None:
        return False
    
    #  тип речи
    if segment_type not in ALLOWED_TYPES:
        return False
    
    # логика времени 
    if segment_start >= segment_end:
        return False
    
    # отсутвие отрицательных чисел
    if segment_start < 0 or segment_end < 0:
        return False
    
    return True

def aggregate_segmentation(segmentation_data: list[dict[str, str | float | None]],
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
    excepted_fields = ["audio_id", "segment_id", "segment_start", "segment_end", "type"]
    valid_data = {}
    audio_ids_re_marking = set()
    had_seen_segments = {}
    
    for segment in segmentation_data:
        for field in excepted_fields:
            segment.setdefault(field, None)
        
        audio_id = segment ["audio_id"]
        segment_id = segment ["segment_id"]
        segment_type = segment["type"]
        segment_start = segment["segment_start"]
        segment_end = segment["segment_end"]
    
        if audio_id is None or audio_id in audio_ids_re_marking:
            continue
        if audio_id in audio_ids_re_marking:
            continue
            
        is_valid = validate_segment (audio_id, segment_id,segment_type,segment_start,segment_end)
        if not is_valid:
            audio_ids_re_marking.add(audio_id)

            if audio_id in valid_data:
                del valid_data[audio_id]
            continue
            
        if segment_id in had_seen_segments:
            exist_audio_id, exist_start,exist_end, exist_type = had_seen_segments[segment_id]
            if (exist_audio_id != audio_id or 
                exist_start != segment_start or 
                exist_end != segment_end or 
                exist_type != segment_type):
                audio_ids_re_marking.add(audio_id)
                
                if exist_audio_id != audio_id:
                    audio_ids_re_marking.add(exist_audio_id)
                
                if audio_id in valid_data:
                    del valid_data[audio_id]
                
                if exist_audio_id in valid_data:
                    del valid_data[exist_audio_id]
                continue
        else:
            had_seen_segments[segment_id] = (audio_id, segment_start, segment_end, segment_type)
        

        if audio_id in audio_ids_re_marking:
            continue
            
        if audio_id not in valid_data:
            valid_data[audio_id] = {}
            
        if segment_start is None and segment_end is None and segment_type is None:
            pass
        else:
            valid_data[audio_id][segment_id] = {
                "start": segment_start,
                "end": segment_end,
                "type": segment_type
            }
    for audio_id in list(valid_data.keys()):
        if audio_id in audio_ids_re_marking:
            del valid_data[audio_id]
    
    return valid_data, list(audio_ids_re_marking)