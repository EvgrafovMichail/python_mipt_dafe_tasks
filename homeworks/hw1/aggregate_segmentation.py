ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    audio_ids_re_marking = []
    valid_segmentation_data = {}

    for segment in segmentation_data:
        # проверка audio_id
        if "audio_id" not in segment:
            continue

        # проверка segment_id
        if "segment_id" not in segment:
            audio_ids_re_marking.append(segment["audio_id"])

            # удаляем невалидный сегмент, если он до этого был валидным
            if segment["audio_id"] in valid_segmentation_data:
                del valid_segmentation_data[segment["audio_id"]]
            continue

        auxiliary_arr = [
            segment.get("segment_start", None),
            segment.get("segment_end", None),
            segment.get("type", None),
        ]

        # голос найден
        if any(auxiliary_arr) and not all(auxiliary_arr) and 0 not in auxiliary_arr:
            audio_ids_re_marking.append(segment["audio_id"])

            if segment["audio_id"] in valid_segmentation_data:
                del valid_segmentation_data[segment["audio_id"]]
            continue

        # обработка фрагмента без голоса
        if not any(auxiliary_arr):
            if segment["audio_id"] in valid_segmentation_data:
                continue

            valid_segmentation_data[segment["audio_id"]] = {}
            continue

        # проверка, что Тип type входит в ALLOWED_TYPES, и тип segment_start / segment_end float
        if (
            (segment.get("type", None) not in ALLOWED_TYPES)
            or (not isinstance(segment.get("segment_start", None), float))
            or (not isinstance(segment.get("segment_end", None), float))
        ):
            audio_ids_re_marking.append(segment["audio_id"])

            if segment["audio_id"] in valid_segmentation_data:
                del valid_segmentation_data[segment["audio_id"]]
            continue

        #  проверка для одного и того же audio_id и segment_id
        #  встречаются ли разные значения start, end или type.
        if (
            segment.get("audio_id", None) in valid_segmentation_data
            and segment.get("segment_id", None) in valid_segmentation_data[segment["audio_id"]]
        ):
            # если совпали
            if list(
                (valid_segmentation_data[segment["audio_id"]][segment["segment_id"]]).values()
            ) == [segment["segment_start"], segment["segment_end"], segment["type"]]:
                continue

            audio_ids_re_marking.append(segment["audio_id"])
            if segment["audio_id"] in valid_segmentation_data:
                del valid_segmentation_data[segment["audio_id"]]
            continue

        if segment["audio_id"] not in valid_segmentation_data:
            valid_segmentation_data[segment["audio_id"]] = {}
        valid_segmentation_data[segment["audio_id"]][segment["segment_id"]] = {
                "start": segment["segment_start"],
                "end": segment["segment_end"],
                "type": segment["type"],
            }

    return valid_segmentation_data, audio_ids_re_marking
