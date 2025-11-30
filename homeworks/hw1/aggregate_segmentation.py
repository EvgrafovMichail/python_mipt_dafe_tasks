ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def _is_segm_valid(segm: list[dict[str, str | float | None]]) -> bool:
    """Функция для проверки сегмента на валидность"""
    segm_start = segm.get("segment_start")
    segm_end = segm.get("segment_end")
    segm_type = segm.get("type")

    if (segm_type is None) or (segm_start is None) or (segm_end is None):
        return False

    if segm_type not in ALLOWED_TYPES:
        return False

    if not (
        isinstance(segm["type"], str)
        and isinstance(segm["segment_start"], float)
        and isinstance(segm["segment_end"], float)
    ):
        return False

    if (segm_start < 0) or (segm_end < 0) or (segm_start > segm_end):
        return False

    return True


def _add_to_valid_data(segm, valid_data):
    """Функция для добавления сегмента в словарь с валидными сегментами"""
    audio_id = segm.get("audio_id")
    segm_id = segm.get("segment_id")
    segm_start = segm.get("segment_start")
    segm_end = segm.get("segment_end")
    segm_type = segm.get("type")

    if audio_id not in valid_data:
        valid_data[audio_id] = {}

    valid_data[audio_id][segm_id] = {
        "start": segm_start,
        "end": segm_end,
        "type": segm_type,
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

    valid_data = {}
    non_valid_audio_id = set()

    for segm in segmentation_data:
        audio_id = segm.get("audio_id")
        segm_id = segm.get("segment_id")
        segm_start = segm.get("segment_start")
        segm_end = segm.get("segment_end")
        segm_type = segm.get("type")

        if audio_id is None:
            continue

        if segm_id is None:
            non_valid_audio_id.add(audio_id)
            continue

        if (segm_type is None) and (segm_start is None) and (segm_end is None):
            if audio_id not in valid_data:
                valid_data[audio_id] = {}
            continue

        if not _is_segm_valid(segm):
            non_valid_audio_id.add(audio_id)

        if (audio_id in valid_data) and (segm_id in valid_data[audio_id]):
            segm_in_valids = valid_data[audio_id][segm_id]

            if (
                (segm_start != segm_in_valids["start"])
                or (segm_end != segm_in_valids["end"])
                or (segm_type != segm_in_valids["type"])
            ):
                non_valid_audio_id.add(audio_id)
                continue

        _add_to_valid_data(segm, valid_data)

    for segm in non_valid_audio_id:
        if segm in valid_data:
            valid_data.pop(segm)

    return valid_data, list(non_valid_audio_id)
