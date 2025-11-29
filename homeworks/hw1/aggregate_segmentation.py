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
    audio_for_remarking = set()
    final_dict = {}
    for dic in segmentation_data:
        if "audio_id" not in dic or dic["audio_id"] is None:
            continue

        audio_id = dic["audio_id"]

        if "segment_id" not in dic or dic["segment_id"] is None:
            audio_for_remarking.add(dic["audio_id"])
            continue

        type_sound = dic["type"]
        start = dic["segment_start"]
        end = dic["segment_end"]
        segment_id = dic["segment_id"]

        # один и тот же сегмент, но разные значения
        if (
            (audio_id in final_dict)
            and (segment_id in final_dict[audio_id])
            and (
                start != final_dict[audio_id][segment_id]["start"]
                or end != final_dict[audio_id][segment_id]["end"]
                or type_sound != final_dict[audio_id][segment_id]["type"]
            )
        ):
            audio_for_remarking.add(audio_id)
            continue

        if type_sound is None and start is None and end is None:
            # это валидный случай - пустой сегмент
            if audio_id not in final_dict:
                final_dict[audio_id] = {}
            final_dict[audio_id][segment_id] = {"start": start, "end": end, "type": type_sound}
            continue

        if (
            (not isinstance(type_sound, str))
            or (not isinstance(start, float))
            or (not isinstance(end, float))
        ):
            audio_for_remarking.add(audio_id)
            continue

        if type_sound not in ALLOWED_TYPES:
            audio_for_remarking.add(audio_id)
            continue

        if audio_id not in final_dict:
            final_dict[audio_id] = {}

        final_dict[audio_id][segment_id] = {"start": start, "end": end, "type": type_sound}

    for audio_id in audio_for_remarking:
        if audio_id in final_dict:
            final_dict.pop(audio_id)

    # аудио пустое, если все параметры каждого сегмента аудио - None
    for audio_key, audio_value in final_dict.items():
        is_empty_audio = True
        for segment_value in audio_value.values():
            if not (
                (segment_value["type"] is None)
                and (segment_value["end"] is None)
                and (segment_value["start"] is None)
            ):
                is_empty_audio = False
                break

        if is_empty_audio:
            final_dict[audio_key] = {}

    return final_dict, list(audio_for_remarking)


"""
lst = []
    final_dict = {}
    for dic in segmentation_data:

        audio_id = dic['audio_id']
        type_sound = dic['type']
        start = dic['segment_start']
        end = dic['segment_end']
        segment_id = dic['segment_id']

        # проверка на наличие аудио в списке некорректных аудио, 
        # на соответствие типов, на наличие None у сегмента
        # (кроме всех значений None у сегмента), проверка допустимости типа речи 
        if  (audio_id in lst) or (
            not "segment_id" in dic) or (
            not isinstance(type_sound, str)) or (
            not isinstance(start, float)) or (
            not isinstance(end, float)) or (
            (type_sound is None or start is None or   #костыль
            end is None) and not (
            type_sound is None and start is None and
            end is None)) or not (
            type_sound in ALLOWED_TYPES):

            lst.append(audio_id)
            continue

        # проверка на повторяющийся сегмент с разными данными
        if audio_id in final_dict and (
            segment_id in final_dict[audio_id]) and (
            final_dict[audio_id][segment_id]['start'] != 
            start or
            final_dict[audio_id][segment_id]['type'] != 
            type_sound or
            final_dict[audio_id][segment_id]['end'] != 
            end):
            
            lst.append(audio_id)
            continue

        
        # для сегмента вообще без данных
        if (type_sound is None and 
            start is None and
            end is None):
                final_dict[audio_id][segment_id] = {}
                continue
        
        if not audio_id in final_dict:
            final_dict[audio_id] = {}

        final_dict[audio_id][segment_id] = {'type' : type_sound, 'start' : start, 'end' : end}
        
            
    return final_dict, lst
"""
