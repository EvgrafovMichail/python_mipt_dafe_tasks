import uuid

ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    valid_data = {}
    invalid_data = set()
    for segment in segmentation_data:
        if (
            "audio_id" in segment.keys()
            and type(segment["audio_id"]) == str
            and segment["audio_id"] != ""
        ):
            lst = [segment["type"], segment["segment_start"], segment["segment_end"]]
            got_segment_id = (
                "segment_id" in segment.keys()
                and type(segment["segment_id"]) == str
                and segment["segment_id"] != ""
            )
            type_type = isinstance(segment["type"], str) or segment["type"] is None
            type_start = (
                isinstance(segment["segment_start"], float) or segment["segment_start"] is None
            )
            type_end = isinstance(segment["segment_end"], float) or segment["segment_end"] is None
            type_None = lst.count(None) == 3 or lst.count(None) == 0
            type_type_allowed = segment["type"] in ALLOWED_TYPES or segment["type"] == None
            if (
                type_type
                and type_start
                and type_end
                and type_None
                and type_type_allowed
                and got_segment_id
            ):  # проверка валидности сегмента
                if (
                    segment["audio_id"] in valid_data.keys()
                    and segment["segment_id"] in valid_data[segment["audio_id"]].keys()
                ):  # проверяем встречали ли мы этот сегмент ранее
                    seg = valid_data[segment["audio_id"]][segment["segment_id"]]
                    if (
                        segment["segment_start"] != seg["start"]
                        or segment["segment_end"] != seg["end"]
                        or segment["type"] != seg["type"]
                    ):  # ищем различия между добавленным ранее сегментом и текущим
                        del valid_data[
                            segment["audio_id"]
                        ]  # нашли различие - удаляем и добавляем audio_id в список невалидных
                        invalid_data.add(segment["audio_id"])
                elif (
                    segment["audio_id"] not in invalid_data
                ):  # проверяем, чтобы audio_id не было в списке невалидных
                    if (
                        segment["audio_id"] not in valid_data.keys()
                    ):  # если не встречали audio_id ранее - создаем новый словарь в valid_data
                        valid_data[segment["audio_id"]] = {}
                    if (
                        segment["segment_start"] != None
                    ):  # только если поля не None, добавляем информацию, иначе игнорируем
                        valid_data[segment["audio_id"]][segment["segment_id"]] = {
                            "start": segment["segment_start"],
                            "end": segment["segment_end"],
                            "type": segment["type"],
                        }
            else:  # работаем с невалидными сегментами
                invalid_data.add(segment["audio_id"])
                if segment["audio_id"] in valid_data.keys():
                    del valid_data[segment["audio_id"]]
    invalid_data = list(invalid_data)

    return valid_data, invalid_data
