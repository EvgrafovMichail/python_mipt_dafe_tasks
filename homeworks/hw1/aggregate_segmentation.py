ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}
print("AAAAAAAAAAAAAAAAAAAAAAAAAa")

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
    audio_ids_with_errors = tuple()
    segment_cache = {}
    
    
    
    for segment in segmentation_data:

        if "segment_id" not in segment or segment["segment_id"] is None:
            continue
            
        if "audio_id" not in segment or segment["audio_id"] is None:
            continue
        
        audio_id = segment["audio_id"]
        segment_id = segment["segment_id"]


        is_valid = True
        

        if not isinstance(segment_id, str):
            is_valid = False
        if not isinstance(audio_id, str):
            is_valid = False


        type_val = segment.get("type")
        start_val = segment.get("segment_start")
        end_val = segment.get("segment_end")
        
        none_count = 0
        for i in [type_val, start_val, end_val]:
            if i is None:
                none_count += 1
        
        if none_count == 1 or none_count == 2:

            is_valid = False
        elif none_count == 0:

            if not isinstance(type_val, str):
                is_valid = False
            elif type_val not in ALLOWED_TYPES:
                is_valid = False
                
            if not isinstance(start_val, float):
                is_valid = False
            if not isinstance(end_val, float):
                is_valid = False


        if not is_valid:
            audio_ids_with_errors = tuple(list(audio_ids_with_errors) + [audio_id])
        else:
            if none_count == 0:
                if audio_id not in valid_data:
                    valid_data[audio_id] = {}
                
                valid_data[audio_id][segment_id] = {
                    "start": start_val,
                    "end": end_val,
                    "type": type_val
                }
            elif none_count == 3:
                if audio_id not in valid_data:
                    valid_data[audio_id] = {}
    
    


    for audio_id in list(valid_data.keys()):
        if audio_id in audio_ids_with_errors:
            del valid_data[audio_id]
            
    
    return valid_data, audio_ids_with_errors
