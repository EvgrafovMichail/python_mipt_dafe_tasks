ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    fields = ["audio_id", "type", "segment_end", "segment_start", "segment_id"]
    valid_data = {}
    audio_ids_re_marking = []  # можно сначала set, потом в лист если не важен порядок сегментов

    for segment in segmentation_data:
        for field in fields:
            segment.setdefault(field, None)
        audio_id = segment["audio_id"]
        segment_id = segment["segment_id"]
        segment_type = segment["type"]
        segment_start = segment["segment_start"]
        segment_end = segment["segment_end"]

        if audio_id is None or audio_id in audio_ids_re_marking:
            continue

        is_valid = True

        if segment_id is None:
            is_valid = False
        elif segment_end is None and segment_start is None and segment_type is None:
            if audio_id not in valid_data:
                valid_data[audio_id] = {}
            continue
        elif not isinstance(segment_type, str):
            is_valid = False
        elif not isinstance(segment_start, (int, float)):
            is_valid = False
        elif not isinstance(segment_end, (int, float)):
            is_valid = False
        elif segment_type not in ALLOWED_TYPES:
            is_valid = False
        elif segment_end is None or segment_start is None or segment_type is None:
            is_valid = False
        elif audio_id in valid_data and segment_id in valid_data[audio_id]:
            existing_segment = valid_data[audio_id][segment_id]
            if (
                existing_segment["type"] != segment_type
                or existing_segment["start"] != segment_start
                or existing_segment["end"] != segment_end
            ):
                is_valid = False

        if not is_valid:
            if audio_id not in audio_ids_re_marking:
                audio_ids_re_marking.append(audio_id)
            if audio_id in valid_data:
                valid_data.pop(audio_id)
            continue

        segment_data = {"type": segment_type, "start": segment_start, "end": segment_end}
        if audio_id not in valid_data:
            valid_data[audio_id] = {}
        valid_data[audio_id][segment_id] = segment_data

    return valid_data, audio_ids_re_marking
