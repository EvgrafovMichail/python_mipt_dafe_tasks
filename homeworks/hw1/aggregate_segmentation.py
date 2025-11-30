ALLOWED_TYPES = {"spotter_word", "voice_human", "voice_bot"}


def is_valid_segment(segment: dict) -> bool:
    seg_type = segment.get("type")
    seg_start = segment.get("segment_start")
    seg_end = segment.get("segment_end")

    if not (isinstance(seg_type, str) or seg_type is None):
        return False
    if not (isinstance(seg_start, float) or seg_start is None):
        return False
    if not (isinstance(seg_end, float) or seg_end is None):
        return False

    if seg_type is None and seg_start is None and seg_end is None:
        return True

    if seg_type is None or seg_start is None or seg_end is None:
        return False

    return seg_type in ALLOWED_TYPES


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    invalid_audio_ids = set()
    seen = {}

    for seg in segmentation_data:
        audio_id = seg.get("audio_id")
        segment_id = seg.get("segment_id")

        if not segment_id:
            if audio_id:
                invalid_audio_ids.add(audio_id)
            continue

        if not audio_id:
            continue

        if not is_valid_segment(seg):
            invalid_audio_ids.add(audio_id)
            continue

        seg_type = seg["type"]
        seg_start = seg["segment_start"]
        seg_end = seg["segment_end"]

        if seg_type is None:
            continue

        key = (audio_id, segment_id)
        triple = (seg_start, seg_end, seg_type)

        if key in seen:
            if seen[key] != triple:
                invalid_audio_ids.add(audio_id)
        else:
            seen[key] = triple

    result = {}

    for seg in segmentation_data:
        audio_id = seg.get("audio_id")
        segment_id = seg.get("segment_id")

        if not audio_id or not segment_id:
            continue

        if audio_id in invalid_audio_ids:
            continue

        if not is_valid_segment(seg):
            continue

        if audio_id not in result:
            result[audio_id] = {}

        seg_type = seg["type"]

        if seg_type is None:
            continue

        result[audio_id][segment_id] = {
            "start": seg["segment_start"],
            "end": seg["segment_end"],
            "type": seg_type,
        }

    return result, sorted(invalid_audio_ids)
