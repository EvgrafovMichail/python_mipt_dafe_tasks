ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data = {}
    audio_ids_remarking = set()

    for segment in segmentation_data:
        audio_id = None if "audio_id" not in segment else segment["audio_id"]
        segment_id = None if "segment_id" not in segment else segment["segment_id"]
        segment_start = None if "segment_start" not in segment else segment["segment_start"]
        segment_end = None if "segment_end" not in segment else segment["segment_end"]
        segment_type = None if "type" not in segment else segment["type"]

        if audio_id is None or audio_id in audio_ids_remarking:
            continue
        if segment_id is None:
            audio_ids_remarking.add(segment["audio_id"])
            continue

        cnt_is_none = 0
        cnt_is_none += segment_type is None
        cnt_is_none += segment_start is None
        cnt_is_none += segment_end is None

        if 0 < cnt_is_none < 3:
            audio_ids_remarking.add(segment["audio_id"])
            continue
        if segment_type is not None and not isinstance(segment_type, str):
            audio_ids_remarking.add(segment["audio_id"])
            continue
        if segment_start is not None and not isinstance(segment_start, float):
            audio_ids_remarking.add(segment["audio_id"])
            continue
        if segment_end is not None and not isinstance(segment_end, float):
            audio_ids_remarking.add(segment["audio_id"])
            continue

        if segment_type is not None and segment_type not in ALLOWED_TYPES:
            audio_ids_remarking.add(segment["audio_id"])
            continue

        if audio_id in valid_data and segment_id in valid_data[audio_id]:
            other_segment = valid_data[audio_id][segment_id]
            segments_are_equal = True
            if not other_segment:
                if segment_type is not None:
                    segments_are_equal = False
            elif (
                segment_type != other_segment["type"]
                or segment_start != other_segment["start"]
                or segment_end != other_segment["end"]
            ):
                segments_are_equal = False
            if not segments_are_equal:
                audio_ids_remarking.add(audio_id)
                continue

        valid_segment = {}
        if segment_type is not None:
            valid_segment["start"] = segment_start
            valid_segment["end"] = segment_end
            valid_segment["type"] = segment_type
        valid_data.setdefault(audio_id, {})
        if valid_segment:
            valid_data[audio_id][segment_id] = valid_segment

    for id in audio_ids_remarking:
        if id in valid_data:
            valid_data.pop(id)

    return valid_data, list(audio_ids_remarking)
