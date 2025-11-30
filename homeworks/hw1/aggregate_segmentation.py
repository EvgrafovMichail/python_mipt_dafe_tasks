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

    # ваш код
    valid: dict[str, dict[str, dict[str, str | float]]] = {}
    seen: dict[tuple[str, str], tuple[float, float, str]] = {}
    to_remark: set[str] = set()

    def ok_type(v) -> bool:
        return v is None or isinstance(v, str)

    def ok_float(v) -> bool:
        return v is None or isinstance(v, float)

    def valid_voice_fields(t, s, e) -> bool:
        return (t is None and s is None and e is None) or (
            t is not None and s is not None and e is not None
        )

    for seg in segmentation_data:
        aid = seg.get("audio_id")
        sid = seg.get("segment_id")
        if not aid or not sid:
            continue

        t = seg.get("type")
        st = seg.get("segment_start")
        en = seg.get("segment_end")

        if not (ok_type(t) and ok_float(st) and ok_float(en)):
            to_remark.add(aid)
            continue

        if not valid_voice_fields(t, st, en):
            to_remark.add(aid)
            continue

        if t is not None and t not in ALLOWED_TYPES:
            to_remark.add(aid)
            continue

        key = (aid, sid)
        if key in seen:
            if seen[key] != (st, en, t):
                to_remark.add(aid)
                continue
            continue

        seen[key] = (st, en, t)

    for (aid, sid), (st, en, t) in seen.items():
        if aid in to_remark:
            continue
        valid.setdefault(aid, {})[sid] = {"start": st, "end": en, "type": t}

    for aid in to_remark:
        valid.pop(aid, None)

    return valid, sorted(to_remark)
