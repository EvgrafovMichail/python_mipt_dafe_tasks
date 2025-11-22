from uuid import UUID

ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def is_valid_uuid(uuid):
    try:
        UUID(uuid)
        return True
    except ValueError:
        return False


def is_valid_segment(segment):
    if "segment_id" not in segment:
        return False

    if not is_valid_uuid(segment["segment_id"]):
        return False

    if (
        segment["type"] is None
        and segment["segment_start"] is None
        and segment["segment_end"] is None
    ):
        pass
    elif (
        not isinstance(segment["type"], str)
        or not isinstance(segment["segment_start"], float)
        or not isinstance(segment["segment_end"], float)
    ):
        return False

    if segment["type"] not in ALLOWED_TYPES and segment["type"] is not None:
        return False

    return True


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

    audio = {}
    not_valid_audio_id = set()

    for i in segmentation_data:
        audio_id = i["audio_id"]
        segment_id = i["segment_id"]
        start = i["segment_start"]
        end = i["segment_end"]
        segment_type = i["type"]

        if is_valid_uuid(audio_id) and is_valid_segment(i):
            if audio_id not in audio:
                audio[audio_id] = {segment_id: {"end": end, "start": start, "type": segment_type}}
            else:
                if segment_id not in audio[audio_id]:
                    audio[audio_id][segment_id] = {"end": end, "start": start, "type": segment_type}
                else:
                    segment = audio[audio_id][segment_id]
                    if (
                        segment["end"] != end
                        or segment["start"] != start
                        or segment["type"] != segment_type
                    ):
                        not_valid_audio_id.add(audio_id)

        else:
            not_valid_audio_id.add(audio_id)

    audio_without_empty_segments = {}
    for a_id, segments in audio.items():
        new_segments = {}
        for s_id, s in segments.items():
            if any(s.values()):
                new_segments[s_id] = s
        audio_without_empty_segments[a_id] = new_segments

    return audio_without_empty_segments, list(not_valid_audio_id)
