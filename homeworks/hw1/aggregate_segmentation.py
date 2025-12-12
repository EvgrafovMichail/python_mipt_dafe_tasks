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

    valid = {}
    problem_audio = set()
    interm_registry  = {} # Дубликаты отсеить и на валидность проверить 
    
    for item in segmentation_data:
        audio_key = item.get('audio_id')
        if audio_key is None:
            continue
            
        segment_key = item.get('segment_id') # Весь audio_id теперь проблемный
        if segment_key is None:
            problem_audio.add(audio_key)
            continue
        
        speech_type = item.get('type')
        start_time = item.get('segment_start')
        end_time = item.get('segment_end')
        
        registry_key = (audio_key, segment_key) # Создаем список
        if registry_key in interm_registry :
            is_already = interm_registry [registry_key] 
            if (is_already['start'] != start_time
                or is_already['end'] != end_time or 
                is_already['type'] != speech_type):
                problem_audio.add(audio_key)
            continue
        
        not_all_none = speech_type is None or start_time is None or end_time is None
        all_none = speech_type is None and start_time is None and end_time is None
        
        if not_all_none and not all_none:
            problem_audio.add(audio_key)
            continue
            
        if not all_none:
            if not isinstance(speech_type, str):
                problem_audio.add(audio_key)
                continue
            if not isinstance(start_time, float) or not isinstance(end_time, float):
                problem_audio.add(audio_key)
                continue
            if speech_type not in ALLOWED_TYPES:
                problem_audio.add(audio_key)
                continue
        
        interm_registry [registry_key] = {
            'start': start_time,
            'end': end_time,
            'type': speech_type
        }
    
    for (audio_id, segment_id), params in interm_registry.items():
        if audio_id in problem_audio:
            continue

        if audio_id not in valid:
            valid[audio_id] = {}
        
        if params['type'] is not None:
            valid[audio_id][segment_id] = {
                'start': params['start'],
                'end': params['end'],
                'type': params['type']
            }
            continue
    
    no_audio = set()
    for item in segmentation_data:
        audio_id = item.get('audio_id')
        if (audio_id not in problem_audio
            and audio_id not in valid):
            no_audio.add(audio_id)
    
    for audio_id in no_audio:
        valid[audio_id] = {}
    
    return valid, list(problem_audio)