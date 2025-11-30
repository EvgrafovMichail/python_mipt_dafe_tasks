import uuid
ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}
def is_valid_segment(segment: dict[str, float | str]) -> bool:   
    type = segment.get('type')
    start = segment.get('segment_start')
    end = segment.get('segment_end')
    
    if 'segment_id' not in segment or segment['segment_id'] is None:
        return False  
    if not segment['type'] and not segment['segment_start'] and not segment['segment_end']:
       return True
    if (not isinstance(type, str) or 
        not isinstance(start, float) or 
        not isinstance(end, float)):
        return False
    if type not in ALLOWED_TYPES:
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
    res_dct = {}
    flag_dct = {}
    #make flag_dct
    for segment in segmentation_data:
        audio_id = segment.get('audio_id')
        
        if audio_id is None:
            continue
        else:
            flag_dct[audio_id] = True
            res_dct[audio_id] = {}
    #validate      
    for segment in segmentation_data:
        audio_id = segment.get('audio_id')
        
        if audio_id is None:
            continue    
        
        segment_id = segment.get('segment_id')
        if not is_valid_segment(segment):
            flag_dct[audio_id] = False
            continue
            
        if segment_id in res_dct[audio_id]:
            past_segment = res_dct[audio_id][segment_id]
            now_segment = {
                'type': segment.get('type'),
                'start': segment.get('segment_start'),
                'end': segment.get('segment_end')
            }
            if (now_segment['end'] != past_segment['end'] or
                now_segment['start'] != past_segment['start'] or
                now_segment['type'] != past_segment['type']):
                flag_dct[audio_id] = False
                continue
            
        else:
            res_dct[audio_id].update({segment_id: 
                {'start': segment['segment_start'], 
                 'end': segment['segment_end'], 
                 'type': segment['type']}})
    #make result
    audio_ids_re_marking = []
    for audio_id in flag_dct:
        if not flag_dct[audio_id]:
            audio_ids_re_marking.append(audio_id)
        for segment_inf in res_dct[audio_id]:
            if res_dct[audio_id][segment_inf]['start'] is None:
                res_dct[audio_id][segment_inf] = {}
            
    return res_dct, audio_ids_re_marking

    

audio_segments = [
    {
        "audio_id": '1100938',
        "segment_id": '0009',
        "segment_start": 5.5,
        "segment_end": 9.5,
        "type": "voice_bot",
    },
    {
        "audio_id": '1100938',
        "segment_id": '0009',
        "segment_start": 5.5,
        "segment_end": 1.5,
        "type": "voice_bot",
    },
    {
        "audio_id": 110,
        "segment_id": str(uuid.uuid4()),
        "segment_start": None,
        "segment_end": None,
        "type": None,
    },
    {
        "audio_id": 110,
        "segment_id": str(uuid.uuid4()),
        "segment_start": 42.0,
        "segment_end": 3.14,
        "type": "voice_bot",
    }
]

valid_data, audio_ids_re_marking = aggregate_segmentation(audio_segments)

#for key in valid_data:
#    print(f"{key}: {valid_data[key]}")

print(audio_ids_re_marking, valid_data)
# {
#     '664c077e-18fd-4e21-8fef-f905a5360786': 
#     {
#         '787e02f5-221d-4f8c-8119-097d22028854': 
#           {'start': 2.0, 'end': 5.5, 'type': 'voice_bot'}
#     }, 
#     'c55c3cd4-8bae-4e5b-ad3d-138a5718332b': 
#     {
#         '18c54b69-f7ce-4c54-9719-a204c1c73ce5': 
#           {'start': 5.5, 'end': 9.5, 'type': 'voice_human'}
#     }
# }