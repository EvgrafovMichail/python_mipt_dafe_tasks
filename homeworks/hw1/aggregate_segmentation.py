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
    segments_by_audio_id = {}
    not_valid_audio_id = set()
    for segm in segmentation_data:
        
        validation = True
        
        type_ = segm.get("type")
        start = segm.get("segment_start")
        end = segm.get("segment_end")
        audio_id = segm.get("audio_id")
        segm_id = segm.get("segment_id")
        all_none = (start is None) and (end is None) and (type_ is None)
        any_none = start is None or end is None or type_ is None
        
        
        if audio_id:
            if audio_id not in segments_by_audio_id:
                segments_by_audio_id[audio_id] = {}
                
            if not segm_id:
                validation = False
            elif all_none:
                validation = True
            elif any_none:
                validation = False
                
            elif not isinstance(end, float) or not isinstance(start, float) or not isinstance(type_, str): 
                validation = False
                
            elif type_ not in ALLOWED_TYPES:
                validation = False
                
            if validation == False:
                not_valid_audio_id.add(audio_id)
                continue
                
            if all_none :
                continue
            
            else:
                new_segment = {"start": start, "end": end, "type": type_}
                if segm_id in segments_by_audio_id[audio_id]:
                    if segments_by_audio_id[audio_id][segm_id] != new_segment:
                        not_valid_audio_id.add(audio_id)
                else: 
                    segments_by_audio_id[audio_id][segm_id] = new_segment
                
                    
    result = {}
    broken_audios = list(not_valid_audio_id)
    for aud_id in segments_by_audio_id:
        if aud_id not in not_valid_audio_id:
            if segments_by_audio_id[aud_id]:
                result[aud_id] = segments_by_audio_id[aud_id]
            else :
                result[aud_id] = {}
    
    
    
    return result, broken_audios
