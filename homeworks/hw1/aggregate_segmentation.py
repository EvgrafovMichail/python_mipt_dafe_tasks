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

    res_dic = {}
    lst_invalid = []
    id_pairs = []
    counter = -1
    global ALLOWED_TYPES
    for dic in segmentation_data:
        counter += 1

        if "audio_id" not in dic:
            continue
        else:
            if "segment_id" not in dic:
                lst_invalid.append(dic["audio_id"])
                continue

            elif (dic["type"] not in ALLOWED_TYPES) and (dic["type"] is not None):
                lst_invalid.append(dic["audio_id"])

                continue


            elif (int(dic["type"] is None) + int(dic["segment_start"] is None) \
                + int(dic["segment_end"] is None)) in (1, 2):
                lst_invalid.append(dic["audio_id"])

                continue

            elif (dic["type"] is None and dic["segment_start"] is None and dic["segment_end"] is None) == False \
                and (isinstance(dic["segment_id"], str) and isinstance(dic["segment_end"], float) \
                and isinstance(dic["segment_start"], float)) == False:
                lst_invalid.append(dic["audio_id"])
                continue




            elif [dic["audio_id"], dic["segment_id"]] in id_pairs:
                index = id_pairs.index([dic["audio_id"], dic["segment_id"]]) + 1
                number = id_pairs[index]
                if (segmentation_data[number]["type"] != dic["type"]) or \
                    (segmentation_data[number]["segment_start"] != dic["segment_start"]) or \
                    (segmentation_data[number]["segment_end"] != dic["segment_end"]):
                    lst_invalid.append(dic["audio_id"])
                    continue
                else:

                    if dic["audio_id"] not in res_dic:
                        res_dic[dic["audio_id"]] = {}
                    if dic["type"] is None and dic["segment_start"] is None and dic["segment_end"] is None:
                        res_dic[dic["audio_id"]][dic["segment_id"]] = {}
                    else:
                        res_dic[dic["audio_id"]][dic["segment_id"]] = {
                            "start": dic["segment_start"],
                            "end": dic["segment_end"],
                            "type": dic["type"]}




            else:

                if dic["audio_id"] not in res_dic:
                    res_dic[dic["audio_id"]] = {}

                if dic["type"] is None and dic["segment_start"] is None and dic["segment_end"] is None:
                    res_dic[dic["audio_id"]][dic["segment_id"]] = {}

                else:
                    res_dic[dic["audio_id"]][dic["segment_id"]] = {
                        "start" : dic["segment_start"],
                        "end" : dic["segment_end"],
                        "type" : dic["type"]}


            if [dic["audio_id"], dic["segment_id"]] not in id_pairs and dic["audio_id"] not in lst_invalid:
                id_pairs.append([dic["audio_id"], dic["segment_id"]])
                id_pairs.append(counter)

    final_res_dic = {}
    for audio_id, segments in res_dic.items():

        all_empty = True
        for segment_data in segments.values():
            if segment_data != {}:
                all_empty = False
                break
        if all_empty == True:
            final_res_dic[audio_id] = {}
        else:
            final_res_dic[audio_id] = segments
    return final_res_dic, lst_invalid

