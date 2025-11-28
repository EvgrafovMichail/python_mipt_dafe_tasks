ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    invalid_audio = set()
    prev_keys = {}
    valid_audio = {}
    for segment in segmentation_data:
        if "audio_id" not in segment:
            continue
        audio_id = segment.get("audio_id", None)
        segment_id = segment.get("segment_id", None)
        start = segment.get("segment_start", None)
        end = segment.get("segment_end", None)
        type = segment.get("type", None)
        invalid = False
        if audio_id in invalid_audio:
            continue
        elif segment_id is None:
            invalid = True
        elif (
            not isinstance(type, str)
            and type is not None
            or not isinstance(start, float)
            and start is not None
            or not isinstance(end, float)
            and end is not None
        ):
            invalid = True
        #    print("типы не соответствуют",segment["audio_id"])
        elif type not in ALLOWED_TYPES and type is not None:
            invalid = True
        elif (end is None or start is None or type is None) and not (
            end is None and start is None and type is None
        ):
            invalid = True
        else:
            key = (audio_id, segment_id)
            if key in prev_keys:
                prev_data = prev_keys[key]
                if (
                    prev_data["type"] != type
                    or prev_data["start"] != start
                    or prev_data["end"] != end
                ):
                    # Нашли конфликт - добавляем audio_id в невалидные
                    invalid = True

            else:
                prev_keys[key] = {"type": type, "start": start, "end": end}

        # действие в зависимости от валидности
        if invalid:
            if audio_id in valid_audio:
                valid_audio.pop(audio_id)
            invalid_audio.add(audio_id)
        elif audio_id in valid_audio:
            if (
                type is not None
            ):  # проверяем только один вместо всех, так как если бы был только один или два,
                # он был бы invalid
                valid_audio[audio_id][segment_id] = {"start": start, "end": end, "type": type}
        else:
            if type is None:
                valid_audio[audio_id] = {}
            else:
                valid_audio[audio_id] = {segment_id: {"start": start, "end": end, "type": type}}
    return valid_audio, list(invalid_audio)
