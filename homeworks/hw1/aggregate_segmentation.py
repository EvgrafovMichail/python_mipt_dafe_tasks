from dataclasses import dataclass
from typing import Dict, List, Set, Tuple, Union

ALLOWED_TYPES: Set[str] = {"int", "float", "str"}

@dataclass
class SegmentationResult:
    data: List[Dict[str, Union[int, float, str]]]
    metadata: Dict[str, Union[int, float, str]]

def aggregate_results(results: List[SegmentationResult]) -> Dict[str, Union[int, float]]:
    if not results:
        return {}
    
    total_items = len(results)
    total_data_length = sum(len(r.data) for r in results)
    avg_data_length = total_data_length / total_items if total_items > 0 else 0.0
    
    aggregated = {
        "total_items": total_items,
        "avg_data_length": float(avg_data_length)
    }
    
    return aggregated

def validate_type(type_name: str) -> bool:
    if not isinstance(type_name, str):
        return False
    
    return type_name in ALLOWED_TYPES

if __name__ == "__main__":
    empty_result = aggregate_results([])
    result1 = SegmentationResult(
        data=[{"id": 1, "value": 0.5}],
        metadata={"version": "1.0"}
    )
    single_result = aggregate_results([result1])
    result2 = SegmentationResult(
        data=[{"id": 2, "value": 0.7}, {"id": 3, "value": 0.8}],
        metadata={"version": "1.0"}
    )
    multiple_result = aggregate_results([result1, result2])