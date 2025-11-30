ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data = {}
    bad_audio_ids = set()
    seen_segments = {}
    audio_seen = set()

    for seg in segmentation_data:
        if "audio_id" not in seg:
            continue

        audio = seg["audio_id"]

        if "segment_id" not in seg:
            bad_audio_ids.add(audio)
            continue

        segment_id = seg["segment_id"]
        start = seg["segment_start"]
        end = seg["segment_end"]
        typ = seg["type"]

        if audio is None:
            continue

        audio_seen.add(audio)

        if segment_id is None:
            bad_audio_ids.add(audio)
            continue

        if start is None and end is None and typ is None:
            continue

        if start is None or end is None or typ is None:
            bad_audio_ids.add(audio)
            continue

        if not isinstance(start, float) or not isinstance(end, float) or not isinstance(typ, str):
            bad_audio_ids.add(audio)
            continue

        if typ not in ALLOWED_TYPES:
            bad_audio_ids.add(audio)
            continue

        key = (audio, segment_id)
        current = (start, end, typ)

        if key in seen_segments and seen_segments[key] != current:
            bad_audio_ids.add(audio)
            for k in list(seen_segments.keys()):
                if k[0] == audio:
                    del seen_segments[k]
            continue

        if audio not in bad_audio_ids:
            seen_segments[key] = current

    for (audio, segment_id), (start, end, typ) in seen_segments.items():
        if audio in bad_audio_ids:
            continue

        if audio not in valid_data:
            valid_data[audio] = {}

        valid_data[audio][segment_id] = {
            "start": start,
            "end": end,
            "type": typ,
        }

    for audio in audio_seen:
        if audio not in bad_audio_ids and audio not in valid_data:
            valid_data[audio] = {}

    return valid_data, list(bad_audio_ids)
