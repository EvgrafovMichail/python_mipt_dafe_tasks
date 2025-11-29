ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data, audio_ids_re_marking = {}, []
    for elem in segmentation_data:
        audio_id = elem.get("audio_id")

        if not audio_id or audio_id in audio_ids_re_marking:
            continue

        segment_id = elem.get("segment_id")

        if not segment_id:
            audio_ids_re_marking.append(audio_id)
            valid_data.pop(audio_id, None)
            continue

        type_val = elem.get("type")
        start_val = elem.get("segment_start")
        end_val = elem.get("segment_end")

        if type_val is None and start_val is None and end_val is None:
            if audio_id not in valid_data:
                valid_data[audio_id] = {}
            continue

        if type_val is None or start_val is None or end_val is None:
            audio_ids_re_marking.append(audio_id)
            valid_data.pop(audio_id, None)
            continue

        if type(type_val) is not str or type(start_val) is not float or type(end_val) is not float:
            audio_ids_re_marking.append(audio_id)
            valid_data.pop(audio_id, None)
            continue

        if type_val not in ALLOWED_TYPES:
            audio_ids_re_marking.append(audio_id)
            valid_data.pop(audio_id, None)
            continue

        if audio_id in valid_data and segment_id in valid_data[audio_id]:
            processed_segment = valid_data[audio_id][segment_id]
            if (
                processed_segment["start"] != start_val
                or processed_segment["end"] != end_val
                or processed_segment["type"] != type_val
            ):
                audio_ids_re_marking.append(audio_id)
                if audio_id in valid_data:
                    valid_data.pop(audio_id, None)
                    continue

        if audio_id not in valid_data:
            valid_data[audio_id] = {}
        valid_data[audio_id][segment_id] = {"start": start_val, "end": end_val, "type": type_val}

    return valid_data, audio_ids_re_marking
