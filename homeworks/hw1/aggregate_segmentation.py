from dataclasses import dataclass
from typing import List, Dict, Union, Any, Tuple, Set, Optional

ALLOWED_TYPES: Set[str] = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}

@dataclass
class SegmentInfo:
    start: float
    end: float
    type: str

def aggregate_segmentation(
    segmentation_data: List[Dict[str, Union[str, float, None]]],
) -> Tuple[Dict[str, Dict[str, Dict[str, Union[str, float]]]], List[str]]:
    
    valid_data: Dict[str, Dict[str, Optional[SegmentInfo]]] = {}
    audio_id_invalid_segments: Set[str] = set()
    obrabotan_segments: Dict[str, Dict[str, Any]] = {}

    for segment in segmentation_data:
        audio_id = segment.get("audio_id")
        segment_id = segment.get("segment_id")

        if not isinstance(audio_id, str) or not audio_id:
            continue
        
        if not isinstance(segment_id, str) or not segment_id:
            audio_id_invalid_segments.add(audio_id)
            continue

        if segment_id in obrabotan_segments:
            duplicate = obrabotan_segments[segment_id]
            
            if (duplicate.get("segment_start") != segment.get("segment_start") or
                duplicate.get("segment_end") != segment.get("segment_end") or
                duplicate.get("type") != segment.get("type")):
                
                audio_id_invalid_segments.add(audio_id)
            continue
        
        type_val = segment.get("type")
        start_val = segment.get("segment_start")
        end_val = segment.get("segment_end")
        
        type_check = isinstance(type_val, (str, type(None)))
        start_check = isinstance(start_val, (float, int, type(None)))
        end_check = isinstance(end_val, (float, int, type(None)))
        
        if not (type_check and start_check and end_check):
            audio_id_invalid_segments.add(audio_id)
            continue

        if isinstance(start_val, int):
            start_val = float(start_val)
        if isinstance(end_val, int):
            end_val = float(end_val)
            
        is_full_segment = (type_val is not None and 
                           start_val is not None and 
                           end_val is not None)
                           
        is_empty_segment = (type_val is None and 
                            start_val is None and 
                            end_val is None)
                            
        if is_full_segment:
            if type_val not in ALLOWED_TYPES:
                audio_id_invalid_segments.add(audio_id)
                continue
        elif not is_empty_segment:
            audio_id_invalid_segments.add(audio_id)
            continue
            
        obrabotan_segments[segment_id] = segment
        
        if audio_id not in valid_data:
            valid_data[audio_id] = {}

        if is_full_segment:
            valid_data[audio_id][segment_id] = {
                "start": start_val,
                "end": end_val,
                "type": type_val
            }
        
    for audio_id_to_remove in audio_id_invalid_segments:
        if audio_id_to_remove in valid_data:
            del valid_data[audio_id_to_remove]
            
    return valid_data, list(audio_id_invalid_segments)