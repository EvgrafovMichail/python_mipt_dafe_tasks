ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data = {}
    audio_id_invalid_segments = set()
    obrabotan_segments = {}

    for segment in segmentation_data:
        if "audio_id" not in segment or not segment["audio_id"]:
            continue

        if "segment_id" not in segment or not segment["segment_id"]:
            audio_id_invalid_segments.add(segment["audio_id"])
            continue

        audio_id = segment["audio_id"]
        segment_id = segment["segment_id"]

        if segment_id in obrabotan_segments:
            dublicat_segment = obrabotan_segments[segment_id]
            if (dublicat_segment["segment_start"] != segment.get("segment_start") or
                dublicat_segment["segment_end"] != segment.get("segment_end") or
                dublicat_segment["type"] != segment.get("type")):
                audio_id_invalid_segments.add(audio_id)
                continue
            else:
                continue
        
        flag_is_valid = True

        if (not isinstance(segment.get("type"), (str, type(None))) or
           (not isinstance(segment.get("segment_start"), (float, type(None)))) or
           (not isinstance(segment.get("segment_end"), (float, type(None))))):
            flag_is_valid = False
        
        type_val = segment.get("type")
        start_val = segment.get("segment_start")
        end_val = segment.get("segment_end")
        
        if type_val is None and start_val is None and end_val is None:
            pass
        else:
            if (type_val is None or start_val is None or end_val is None):
                flag_is_valid = False
            elif (type_val is not None and type_val not in ALLOWED_TYPES):
                flag_is_valid = False
        
        if not flag_is_valid:
            audio_id_invalid_segments.add(audio_id)
            continue
        
        obrabotan_segments[segment_id] = segment

        if audio_id not in valid_data:
            valid_data[audio_id] = {}
        
        if type_val is not None and start_val is not None and end_val is not None:
            valid_data[audio_id][segment_id] = {
                "start": start_val,
                "end": end_val,
                "type": type_val
            }
    
    for audio_id_to_remove in audio_id_invalid_segments:
        if audio_id_to_remove in valid_data:
            del valid_data[audio_id_to_remove]
        
    return valid_data, list(audio_id_invalid_segments)