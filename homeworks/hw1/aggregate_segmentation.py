ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}



def check_validation(audio_segment: dict, used_id: list[list[str, str]]) -> list[bool, int]:
    """Проверка данных на валидность 
            Args:
                audio_segment: словарь, в котором хранится сегемент который в данный момент находится на проверкеимеет те же поля, что и segmentation_data
                used_id : cписок сегментов прошедших проверку хранит внутри массивы в каждом из которых первыйм идет audio_id вторым segment_id
            Return:
                [True,0] если значение валидно и на всех полях не None
                [True,1] если значение валидно и на во всех полях None
                [False,0] если значение невалидно

    """


    required_keys: tuple = ("segment_id", "segment_start", "segment_end", "type")

    if not all(k in audio_segment for k in required_keys):
        return [False, 0]

    if not isinstance(audio_segment["segment_id"], str):
        return [False, 0]

    start: float = audio_segment["segment_start"]
    end: float = audio_segment["segment_end"]
    audio_type: str = audio_segment["type"]

    if all(v is None for v in (start, end, audio_type)):
        return [True, 1]

    if any(v is None for v in (start, end, audio_type)):
        return [False, 0]

    if not isinstance(start, float) or not isinstance(end, float) or not isinstance(audio_type, str):
        return [False, 0]
    

    if audio_segment["type"] not in ALLOWED_TYPES:
        return [False, 0]
    
    id_check = [audio_segment["audio_id"], audio_segment["segment_id"]]


    return [not(id_check in used_id),0]





def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
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
    result : list[dict[str, dict[str, dict[str, str | float]]], list[str]] = [{}, []]
    audio_id_set = set(i["audio_id"] for i in segmentation_data)
    redo_set: set = set()
    used_id : list[list] = []


    unique_segments: list = [] #удаляем прям одинаковые элементы чтобы потом не проверять
    unique_segments_checked: set = set()
    for segment in segmentation_data: 
        key = tuple(sorted(segment.items())) #делаем tuple чтобы добавлять в множество тк массив нельзя(чтобы не забыть на сдаче)
        if key not in unique_segments_checked:
            unique_segments_checked.add(key)
            unique_segments.append(segment)
    segmentation_data = unique_segments




    for audio in audio_id_set:
        audio_rn: dict = {}
        for segment in segmentation_data:
            if segment["audio_id"] == audio:
                checker = check_validation(segment, used_id)
                if checker[0] and checker[1] == 0:
                    audio_rn[segment["segment_id"]] = {"start": segment["segment_start"], "end" : segment["segment_end"],
                                                       "type" : segment["type"]}
                    used_id.append([segment["audio_id"],segment["segment_id"]])
                elif checker[0] and checker[1] == 1:
                    used_id.append([segment["audio_id"],segment["segment_id"]])
                else:
                    redo_set.add(audio)
                    break
        if audio in redo_set:
            continue
        result[0][audio] = audio_rn
    result[1] = list(redo_set)
    return tuple(result)
