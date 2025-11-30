ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:

    bad_audio_ids_set = set() # СМ 55
    all_audio_ids = set() # СМ 55

    for item in segmentation_data:
        
        if "audio_id" not in item or item["audio_id"] is None:
            continue
        
        aud_id = item["audio_id"] # СМ 4
        all_audio_ids.add(aud_id) # СМ 56

        # Проверка наличия всех обязательных ключей и их значений None
        if "segment_start" not in item or item["segment_start"] is None or \
           "segment_end" not in item or item["segment_end"] is None or \
           "type" not in item or item["type"] is None: # ЧТД 45, 21
             continue
        
        if item["segment_start"] >= item["segment_end"]: # ЧТД 44
            bad_audio_ids_set.add(aud_id) # СМ 56
        
        if item["type"] not in ALLOWED_TYPES: # СМ 26, 56
            bad_audio_ids_set.add(aud_id)

    result_dict = {} # СМ 4
    
    for item in segmentation_data:
        
        if "audio_id" not in item or "segment_id" not in item or "segment_start" not in item or "segment_end" not in item or "type" not in item:
            continue

        aud_id = item["audio_id"] # СМ 4
        seg_id = item["segment_id"] # СМ 4
        s_start = item["segment_start"] # СМ 4
        s_end = item["segment_end"] # СМ 4
        s_type = item["type"] # СМ 4

        if aud_id is None or seg_id is None or s_start is None or s_end is None or s_type is None:
            continue

        if aud_id in bad_audio_ids_set: # СМ 26
            continue
            
        if s_start >= s_end or s_type not in ALLOWED_TYPES: # ЧТД 44
            continue

        if aud_id not in result_dict: # СМ 26
            result_dict[aud_id] = {} # СМ 4
            
        result_dict[aud_id][seg_id] = { # СМ 4
            "start": s_start,
            "end": s_end,
            "type": s_type
        }

    for aud_id in all_audio_ids: # СМ 21
        if aud_id not in bad_audio_ids_set and aud_id not in result_dict: # СМ 26
            result_dict[aud_id] = {} # СМ 4

    bad_ids_list = list(bad_audio_ids_set) # ПФ 51
    
    return result_dict, bad_ids_list # ПФ 51