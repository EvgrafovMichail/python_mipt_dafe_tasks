#import uuid

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
    valid_audios = {}
    invalid_audios = set()

    def make_invalid(aid: str) -> None:
        invalid_audios.add(aid)

        if aid in valid_audios:
            valid_audios.pop(aid)

    for segment_data in segmentation_data:
        audio_id = segment_data.get("audio_id")

        if not audio_id:
            continue

        segment_id = segment_data.get("segment_id")

        if not segment_id:
            make_invalid(audio_id)
            continue

        segment_type = segment_data.get("type")
        segment_start = segment_data.get("segment_start")
        segment_end = segment_data.get("segment_end")

        if segment_type is None and segment_start is None and segment_end is None:
            valid_audios.setdefault(audio_id, {})
            continue

        if segment_type is None or segment_start is None or segment_end is None:
            make_invalid(audio_id)
            continue

        if (
            not isinstance(segment_type, str)
            or not isinstance(segment_start, float)
            or not isinstance(segment_end, float)
        ):
            make_invalid(audio_id)
            continue

        if segment_type not in ALLOWED_TYPES:
            make_invalid(audio_id)
            continue

        if audio_id in valid_audios and segment_id in valid_audios[audio_id]:
            cope = valid_audios[audio_id][segment_id]
            if (
                cope["start"] != segment_start
                or cope["end"] != segment_end
                or cope["type"] != segment_type
            ):
                make_invalid(audio_id)
                continue

        if audio_id not in valid_audios:
            valid_audios.setdefault(audio_id, {})

        valid_audios[audio_id][segment_id] = dict(
            start=segment_start, end=segment_end, type=segment_type
        )
        
    invalid_audios_lst = list(invalid_audios)
    return valid_audios, invalid_audios_lst
