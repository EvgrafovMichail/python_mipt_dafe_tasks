ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:

    bad_audio_ids_set = set()
    all_audio_ids = set()

    for item in segmentation_data:
        
        if "audio_id" not in item or item["audio_id"] is None:
            continue
        
        aud_id = item["audio_id"]
        all_audio_ids.add(aud_id)

        if "segment_start" not in item or item["segment_start"] is None or \
           "segment_end" not in item or item["segment_end"] is None or \
           "type" not in item or item["type"] is None:
             continue
        
        if item["segment_start"] >= item["segment_end"]:
            bad_audio_ids_set.add(aud_id)
        
        if item["type"] not in ALLOWED_TYPES:
            bad_audio_ids_set.add(aud_id)

    result_dict = {}
    
    for item in segmentation_data:
        
        if "audio_id" not in item or "segment_id" not in item or "segment_start" not in item or "segment_end" not in item or "type" not in item:
            continue

        aud_id = item["audio_id"]
        seg_id = item["segment_id"]
        s_start = item["segment_start"]
        s_end = item["segment_end"]
        s_type = item["type"]

        if aud_id is None or seg_id is None or s_start is None or s_end is None or s_type is None:
            continue

        if aud_id in bad_audio_ids_set:
            continue
            
        if s_start >= s_end or s_type not in ALLOWED_TYPES:
            continue

        if aud_id not in result_dict:
            result_dict[aud_id] = {}
            
        result_dict[aud_id][seg_id] = {
            "start": s_start,
            "end": s_end,
            "type": s_type
        }

    for aud_id in all_audio_ids:
        if aud_id not in bad_audio_ids_set and aud_id not in result_dict:
            result_dict[aud_id] = {}

    bad_ids_list = list(bad_audio_ids_set)
    
    return result_dict, bad_ids_list