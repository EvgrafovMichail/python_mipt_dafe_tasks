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

    #Словарь с валидными сегментами, объединёнными по `audio_id`;
    valid_audio: dict[str, dict[str, dict[str, str | float]]] = {}

    #Множество `audio_id` (str), которые требуют переразметки.
    invalid_audio: set[str] = set()

    #Проверка на невалидность audio_id с помощью поиска невалидных сегментов
    #В valid_audio хранятся все audio_id с сегментами, 
    #которые при нынешней итерации валидны и те, что добавлены в множество невалидных
    for segment in segmentation_data:

        #Проверка на отсутствующий id
        if segment["audio_id"] != "":
            
            #Проверка на валидность audio
            if segment["audio_id"] in invalid_audio: continue

            #Проверка на валидность сегмента по первым четырем критерям
            if  not validate_segment(segment):
                invalid_audio.add(segment["audio_id"]) 
                continue

            #Проверка ключа и создание для него значения одновременно
            #Мы также добавляем и пустые сегменты !!!
            if (valid_audio.setdefault(segment["audio_id"], {})):
                
                #Проверка на совпадение сегментов
                #segment не имеет неправильного совпадения в valid_audio
                if compare_segments(segment, valid_audio):
                    add_segment(segment, valid_audio)

                #Нашлось неправильное совпадение
                else:
                    invalid_audio.add(segment["audio_id"])

            else:
                #Добавление первого сегмента
                add_segment(segment, valid_audio)

    #Сборка valid_audio по всем критериям валидности сегмента
    #Здесь пустые сегменты не учитываются !!!
    valid_audio = {}
    for segment in segmentation_data:

        if segment["audio_id"] != "" and segment["audio_id"] not in invalid_audio:
            valid_audio.setdefault(segment["audio_id"], {})

            if not is_empty(segment):
                add_segment(segment, valid_audio)

    #Кортеж со словарем с валидными сегментами и списком с невалидными audio_id
    return valid_audio, list(invalid_audio)

def validate_segment(
    segment: dict[str, str | float | None] 
) -> bool:
    
    return (

        # 1.Проверка на отсутствие id
        segment["segment_id"] != "" and

        # 2.Проверка на корректность типов
        isinstance(segment["segment_start"], (float, type(None))) and
        isinstance(segment["segment_end"], (float, type(None))) and
        isinstance(segment["type"], (str, type(None))) and

        # 3.Проверка на None
        ((  # 1-ый случай
            segment["segment_start"] is not None and 
            segment["segment_end"] is not None and
            segment["type"] is not None and

            # 4.Проверка type на типы из ALLOWED_TYPES
            segment["type"] in ALLOWED_TYPES
        )
        or
        (   # 2-ой случай
            is_empty(segment)
        ))

    )

#5 Проверка на единственность
def compare_segments(
    standart_segment: dict[str, str | float | None], 
    audio: dict[str, dict[str, dict[str, str | float]]]
) -> bool:

    audio_segments = audio[standart_segment["audio_id"]]
    if standart_segment["segment_id"] in audio_segments.keys():

        segment_values = audio_segments[standart_segment["segment_id"]]
        return (
            segment_values["start"] == standart_segment["segment_start"] and
            segment_values["end"] == standart_segment["segment_end"] and
            segment_values["type"] == standart_segment["type"]
        )

    return True

def add_segment(
    segment: dict[str, str | float | None], 
    audio: dict[str, dict[str, dict[str, str | float]]]
) -> None:

    audio[segment["audio_id"]][segment["segment_id"]] = {
        "start": segment["segment_start"],
        "end": segment["segment_end"],
        "type": segment["type"]
    }

def is_empty(segment: dict[str, str | float | None]) -> bool:

    return (
        segment["segment_start"] is None and
        segment["segment_end"] is None and
        segment["type"] is None
    )