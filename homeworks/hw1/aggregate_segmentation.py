ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, float | str]]], list[str]]:
    """
    Функция для валидации и агрегации данных разметки аудио сегментов.

    Args:
        segmentation_data: словарь, данные разметки аудиосегментов с полями:
            "audio_id" - уникальный идентификатор аудио.
            "segment_id" - уникальный идентификатор сегмента.
            "segment_start" - время начала сегмента.
            "segment_end" - время окончания сегмента.
            "type" - тип голоса в сегменте.

    Returns:
        Словарь с валидными сегментами, объединёнными по `audio_id`;
        Список `audio_id` (str), которые требуют переразметки.
    """

    temp_data = {}
    invalid_audio = set()
    registry = {}

    for seg in segmentation_data:
        audio_id = seg.get("audio_id")
        seg_id = seg.get("segment_id")

        if audio_id is None:
            continue

        if seg_id is None:
            invalid_audio.add(audio_id)
            continue

        start = seg.get("segment_start")
        end = seg.get("segment_end")
        typ = seg.get("type")

        no_voice = start is None and end is None and typ is None
        ok = True

        if not no_voice:
            if start is None or end is None or typ is None:
                ok = False
            elif (
                not isinstance(start, float)
                or not isinstance(end, float)
                or not isinstance(typ, str)
            ):
                ok = False
            elif typ not in ALLOWED_TYPES:
                ok = False

        key = (audio_id, seg_id)
        curr_repr = (start, end, typ)
        if key in registry and registry[key] != curr_repr:
            ok = False
        else:
            registry[key] = curr_repr

        if not ok:
            invalid_audio.add(audio_id)
            temp_data.pop(audio_id, None)
            continue

        if audio_id not in temp_data:
            temp_data[audio_id] = {}

        if not no_voice:
            temp_data[audio_id][seg_id] = {"start": start, "end": end, "type": typ}
        else:
            if audio_id not in temp_data:
                temp_data[audio_id] = {}

    valid_data = {}
    for aid, segs in temp_data.items():
        if aid not in invalid_audio:
            valid_data[aid] = segs

    return valid_data, sorted(invalid_audio)
