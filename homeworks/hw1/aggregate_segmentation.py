from dataclasses import dataclass
from typing import Any, Dict, List, Set, Tuple, Union

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
    
    valid_data: Dict[str, Dict[str, Dict[str, Union[str, float]]]] = {}
    invalid_segments: List[str] = []
    
    return valid_data, invalid_segments