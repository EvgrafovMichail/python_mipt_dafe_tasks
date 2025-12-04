
ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def is_not_valid_segment(segment: dict[str, str | float | None]) -> bool:
    if (
        not isinstance(segment.get("type"), (str, type(None)))
        or not isinstance(segment.get("segment_start"), (float, type(None)))
        or not isinstance(segment.get("segment_end"), (float, type(None)))
    ):
        return True

    segment_type = segment.get("type")
    segment_start = segment.get("segment_start")
    segment_end = segment.get("segment_end")

    if (segment_type is None) and (segment_start is None) and (segment_end is None):
        return False

    if (segment_type is None) or (segment_start is None) or (segment_end is None):
        return True

    if (segment_type is not None) and (segment_type not in ALLOWED_TYPES):
        return True

    return False


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    not_valid_list = []
    res_dct = {}

    for segment in segmentation_data:
        if not segment.get("segment_id"):
            if segment.get("audio_id"):
                not_valid_list.append(segment["audio_id"])
            continue

        if not segment.get("audio_id"):
            continue

        audio_id = segment["audio_id"]
        segment_id = segment["segment_id"]
        
        if audio_id in not_valid_list:
            continue

        if is_not_valid_segment(segment):
            if audio_id not in not_valid_list:
                not_valid_list.append(audio_id)

            if audio_id in not_valid_list:
                del res_dct[audio_id]
            continue

        segment_type = segment.get("type")
        segment_start = segment.get("segment_start")
        segment_end = segment.get("segment_end")

        if (segment_type is None) and (segment_start is None) and (segment_end is None):
            if audio_id not in res_dct:
                res_dct[audio_id]= {segment_id: {}}
            else: 
                res_dct[audio_id][segment_id] = {}
            continue
            
        if audio_id in res_dct:
            if segment_id in res_dct[audio_id]:
                curr_seg = res_dct[audio_id][segment_id]

                if (
                    segment_start != curr_seg["start"]
                    or segment_end != curr_seg["end"]
                    or segment_type != curr_seg["type"]
                ):
                    if audio_id not in not_valid_list:
                        not_valid_list.append(audio_id)
                        
                    if audio_id in not_valid_list:
                        del res_dct[audio_id]
            else:
                res_dct[audio_id][segment_id] = {
                    "start": segment_start,
                    "end": segment_end,
                    "type": segment_type,
                }
        else:
            res_dct[audio_id] = {
                segment_id: {"start": segment_start, "end": segment_end, "type": segment_type}
            }
            
    for _audio_id in res_dct: 
        len_res_dict = len(res_dct[_audio_id])
        count_empty = 0
        for _segment_id in res_dct[_audio_id]:
            if res_dct[_audio_id][_segment_id] == {}: 
                count_empty += 1
        if count_empty == len_res_dict:
            res_dct[_audio_id] = {}

    return res_dct, not_valid_list





