ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
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
    val = {}
    neval = []
    check_dubl = {}

    def valid_data(data):
        audio_id = data["audio_id"]
        seg_id = data["segment_id"]
        start = data["segment_start"]
        end = data["segment_end"]
        typ = data["type"]


        if seg_id is None:
            return False

        if start is None and end is None and typ is None:
            return {}

        if start is None or end is None or typ is None:
            return False

        if (type(start) != type(1.0)) or (type(end) != type(1.0)) or (type(typ) != type(" ")):
            return False

        if typ not in ALLOWED_TYPES:
            return False

        znach = {"start": start, "end": end, "type": typ}

        if (audio_id, seg_id) in check_dubl:
            if check_dubl[(audio_id, seg_id)] != znach:
                return False
        else:
            check_dubl[(audio_id, seg_id)] = znach

        return True

    for data in segmentation_data:
        if "audio_id" not in data:
            continue

        check = valid_data(data)

        if check == {}:
            val.setdefault(data["audio_id"], {})
            continue

        elif check:
            audio_id = data["audio_id"]
            seg_id = data["segment_id"]

            if audio_id not in val:
                val[audio_id] = {}

            val[audio_id][seg_id] = {
                "start": data["segment_start"],
                "end": data["segment_end"],
                "type": data["type"],
            }
            continue

        else:
            neval.append(data["audio_id"])

    for i in neval:
        val.pop(i, None)

    neval = list(set(neval))
    return val, neval
