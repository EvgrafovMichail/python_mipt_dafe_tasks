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
    to_remark: set[str] = set()
    seen: dict[tuple[str, str], tuple[float | None, float | None, str | None]] = {}

    def ok_type(v):
        return v is None or isinstance(v, str)

    def ok_float(v):
        return v is None or isinstance(v, float)

    for seg in segmentation_data:
        aid = seg.get("audio_id")
        sid = seg.get("segment_id")
        if not aid or not sid:
            continue
        t, st, en = seg.get("type"), seg.get("segment_start"), seg.get("segment_end")

        if not (ok_type(t) and ok_float(st) and ok_float(en)):
            to_remark.add(aid)
            continue
        all_none = t is None and st is None and en is None
        any_none = t is None or st is None or en is None
        if any_none and not all_none:
            to_remark.add(aid)
            continue
        if t is not None and t not in ALLOWED_TYPES:
            to_remark.add(aid)
            continue

        key = (aid, sid)
        if key in seen and seen[key] != (st, en, t):
            to_remark.add(aid)
            continue
        seen[key] = (st, en, t)

    for (aid, sid), (st, en, t) in seen.items():
        if aid in to_remark or t is None:
            continue
        valid.setdefault(aid, {})[sid] = {"start": st, "end": en, "type": t}

    for aid in {aid for (aid, _), (_, _, t) in seen.items() if t is None}:
        if aid not in to_remark:
            valid.setdefault(aid, {})

    return valid, sorted(to_remark)
