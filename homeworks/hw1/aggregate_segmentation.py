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
    A_UI = "audio_id"  # - уникальный идентификатор аудио.
    S_UI = "segment_id"  # - уникальный идентификатор сегмента.
    S_ST = "segment_start"  # - время начала сегмента.
    S_END = "segment_end"  # - время окончания сегмента.
    S_T = "type"  # - тип голоса в сегменте.

    valid = {}
    invalid = []

    for i in segmentation_data:
        if i[A_UI] in invalid:
            continue

        if not i.get(A_UI):
            continue

        if not i.get(S_UI):
            invalid.append(i[A_UI])
            continue

        if i[A_UI] not in valid:
            valid[i[A_UI]] = {}

        if i[A_UI] in valid:
            if i[S_UI] in valid[i[A_UI]]:
                if (
                    i[S_ST] == valid[i[A_UI]][i[S_UI]]["start"]
                    and i[S_END] == valid[i[A_UI]][i[S_UI]]["end"]
                    and i[S_T] == valid[i[A_UI]][i[S_UI]]["type"]
                ):
                    continue
                else:
                    if i[A_UI] in valid:
                        del valid[i[A_UI]]

                    invalid.append(i[A_UI])
                    continue

        if not i[S_ST] and not i[S_END] and not i[S_T]:
            if i[A_UI] in valid:
                continue

            valid[i[A_UI]] = {}

        if (
            i[S_T] in ALLOWED_TYPES
            and isinstance(i[S_T], str)
            and isinstance(i[S_ST], float)
            and isinstance(i[S_END], float)
        ):
            valid[i[A_UI]][i[S_UI]] = {"start": i[S_ST], "end": i[S_END], "type": i[S_T]}
        else:
            if i[A_UI] in valid:
                del valid[i[A_UI]]
            invalid.append(i[A_UI])

    return valid, invalid
