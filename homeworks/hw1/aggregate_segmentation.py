from dataclasses import asdict, dataclass

ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


@dataclass
class Segment:
    segment_id: str

    segment_start: float
    segment_end: float

    audio_id: str
    type: str


class SegmentValidator:
    segments: dict[tuple[str, str], Segment]

    def __init__(self):
        self.segments = {}

    @staticmethod
    def type_validator(segment: Segment):
        segment_dict = asdict(segment)

        types = {
            "segment_id": str,
            "audio_id": str,
            "type": (str, type(None)),
            "segment_start": (float, type(None)),
            "segment_end": (float, type(None)),
        }

        return all(
            isinstance(segment_dict[field], field_type) for field, field_type in types.items()
        )

    @staticmethod
    def value_validator(segment: Segment):
        type = segment.type

        if type not in ALLOWED_TYPES:
            return False

        if SegmentValidator.has_none(segment):
            return False

        return True

    @staticmethod
    def is_segment_empty(segment: Segment):
        fields = (segment.segment_start, segment.segment_end, segment.type)

        return all(x is None for x in fields)

    @staticmethod
    def has_none(segment: Segment):
        fields = (segment.segment_start, segment.segment_end, segment.type)

        return any(x is None for x in fields)

    def is_unique(self, segment: Segment):
        key = (segment.audio_id, segment.segment_id)

        if key in self.segments:
            last = self.segments[key]

            if (
                last.segment_start != segment.segment_start
                or last.segment_end != segment.segment_end
                or last.type != segment.type
            ):
                return False

        else:
            self.segments[key] = segment

        return True

    def validate(self, segment: Segment):
        if SegmentValidator.is_segment_empty(segment):
            return True

        validators = [self.value_validator, self.type_validator, self.is_unique]

        return all(validator(segment) for validator in validators)


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

    valid_audio: dict[str, dict[str, dict[str, str | float]]] = {}
    ids_re_marking: set[str] = []

    validator = SegmentValidator()

    for item in segmentation_data:
        audio_id = item.get("audio_id", None)

        if audio_id is None or audio_id in ids_re_marking:
            continue

        if "segment_id" not in item:
            ids_re_marking.append(audio_id)
            continue

        segment = Segment(**item)

        if not validator.validate(segment):
            ids_re_marking.append(audio_id)
            continue

        if audio_id not in valid_audio:
            valid_audio[audio_id] = {}

        if SegmentValidator.is_segment_empty(segment):
            continue

        valid_audio[audio_id][segment.segment_id] = {
            "start": segment.segment_start,
            "end": segment.segment_end,
            "type": segment.type,
        }

    for to_re_marking in ids_re_marking:
        valid_audio.pop(to_re_marking, None)

    return valid_audio, list(ids_re_marking)
