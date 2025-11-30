ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    passing_segment = {}
    wrong_segment = set()
    repeating_segment = {}
    
    for i in range(len(segmentation_data)):
        segment = segmentation_data[i]
        audio_id = segment.get("audio_id")
        
        if audio_id is None:
            continue
            
        segment_id = segment.get("segment_id")
        if segment_id is None:
            wrong_segment.add(audio_id)
            continue
            
        segment_start = segment.get("segment_start")
        segment_end = segment.get("segment_end")
        segment_type = segment.get("type")
        
        if segment_start is None and segment_end is None and segment_type is None:
            if audio_id not in passing_segment:
                passing_segment[audio_id] = {}
            continue
            
        if type(segment_start) != float or type(segment_end) != float or type(segment_type) != str:
            wrong_segment.add(audio_id)
            continue
            
        if segment_type not in ALLOWED_TYPES:
            wrong_segment.add(audio_id)
            continue
            
        if segment_end >= segment_start or segment_end < 0 or segment_start < 0:
            wrong_segment.add(audio_id)
            continue
            
        key = (audio_id, segment_id)
        
        if key in repeating_segment:
            old_data = repeating_segment[key]
            if (old_data["segment_start"] != segment_start or 
                old_data["segment_end"] != segment_end or 
                old_data["type"] != segment_type):
                wrong_segment.add(audio_id)
                continue
        else:
            repeating_segment[key] = {
                "type": segment_type, 
                "start": segment_start, 
                "end": segment_end
            }
            
        if audio_id not in passing_segment:
            passing_segment[audio_id] = {}
            
        passing_segment[audio_id][segment_id] = {
            "type": segment_type, 
            "start": segment_start, 
            "end": segment_end
        }
    
    for bad_audio in wrong_segment:
        if bad_audio in passing_segment:
            del passing_segment[bad_audio]
            
    wrong_list = []
    for item in wrong_segment:
        wrong_list.append(item)
        
    return passing_segment, wrong_list