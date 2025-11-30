ALLOWED_TYPES = {
    "spotter_word",
    "voice_human",
    "voice_bot",
}


def aggregate_segmentation(
    segmentation_data: list[dict[str, str | float | None]],
) -> tuple[dict[str, dict[str, dict[str, str | float]]], list[str]]:
    resdict = {}
    backlist = []
    removelist = []

    for onefragm in segmentation_data:
        audid, segid = onefragm["audio_id"], onefragm["segment_id"]
        if not audid:
            continue
        if segid:
            start, end, ttype = onefragm["segment_start"], onefragm["segment_end"], onefragm["type"]
            if start is None and end is None and ttype is None:
                if audid in resdict:
                    resdict[audid][segid] = {}
                else:
                    resdict[audid] = {segid: {}}
            elif bool(ttype is not None and start is not None and end is not None) or (not
                bool(ttype is not None or start is not None or end is not None)):
                if type(start) is float and type(end) is float and type(ttype) is str:
                    if ttype in ALLOWED_TYPES:
                        if audid in resdict and audid not in removelist:
                            if segid in resdict[audid]:
                                if (
                                    start == resdict[audid][segid]["start"]
                                    and end == resdict[audid][segid]["end"]
                                    and ttype == resdict[audid][segid]["type"]
                                ):
                                    pass
                                else:
                                    del resdict[audid]
                                    backlist.append(audid)
                                    removelist.append(audid)
                            else:
                                resdict[audid][segid] = {"start": start, "end": end, "type": ttype}
                        else:
                            if audid not in removelist:
                                resdict[audid] = {
                                    segid: {"start": start, "end": end, "type": ttype}
                                }

                    else:
                        backlist.append(audid)
                else:
                    backlist.append(audid)
            else:
                backlist.append(audid)
        else:
            backlist.append(audid)

    for audid in resdict:
        flaglist = [1 for segm in resdict[audid] if resdict[audid][segm]]
        if 1 not in flaglist:
            resdict[audid] = {}

    return resdict, backlist
