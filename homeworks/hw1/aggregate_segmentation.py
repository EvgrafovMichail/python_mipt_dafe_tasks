

ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}

def is_segment_valid(audio_id, segment_id, segment_type, segment_start, segment_end):

    if audio_id is None or segment_id is None:
        return False
    
    if segment_start is not None and not isinstance(segment_start, float):
        return False
    
    if segment_end is not None and not isinstance(segment_end, float):
        return False
    
    all_none = (segment_type is None and segment_start is None and segment_end is None )
    any_none = (segment_type is None or segment_start is None or segment_end is None )
     
    if any_none and (not all_none) :
        return False 
    
    if segment_type is not None and segment_type not in ALLOWED_TYPES:
        return False
    
    return True

def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data = {} 
    audio_ids_for_remarking = set() 
    seen_segments = {}  

    for segment in segmentation_data:

        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")
        segment_start = segment.get("segment_start")
        segment_end = segment.get("segment_end")
        segment_type = segment.get("type")

        if audio_id is None:
            continue
        
        if audio_id in audio_ids_for_remarking:
            continue

        is_valid = is_segment_valid(audio_id, segment_id, segment_type, segment_start, segment_end)

        if not is_valid:
            audio_ids_for_remarking.add(audio_id)
            if audio_id in valid_data:
                del valid_data[audio_id]
            continue


        if (audio_id, segment_id) in seen_segments:
            existing_data = seen_segments[(audio_id, segment_id)]
            if (existing_data["start"] != segment_start or 
                existing_data["end"] != segment_end or 
                existing_data["type"] != segment_type):
                audio_ids_for_remarking.add(audio_id)
                if audio_id in valid_data:
                    del valid_data[audio_id]
                continue
        else:
            seen_segments[(audio_id, segment_id)] = {
            "start": segment_start,
            "end": segment_end, 
            "type": segment_type
            }
        if audio_id not in valid_data and audio_id not in audio_ids_for_remarking:
            valid_data[audio_id] = {}

        #проверить сегмент без рeчи
        all_none = (segment_type is None and segment_start is None and segment_end is None)


        if not all_none:
             valid_data[audio_id][segment_id] = {
                "start": segment_start,
                "end": segment_end,
                "type": segment_type
            }
    audio_ids_re_marking = list(audio_ids_for_remarking)

    return valid_data, audio_ids_re_marking

