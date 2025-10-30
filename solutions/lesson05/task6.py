def simplify_path(path: str) -> str:
    # ваш код
    segments = path.split("/")
    segment_to_remove = ["", "."]
    filtered = []
    for i in segments:
        if i not in segment_to_remove:
            filtered.append(i)

    result = []
    for segment in filtered:
        if segment == "..":
            if len(result) > 0:
                result.pop()
            else:
                return ""
        else:
            result.append(segment)

    if not result:
        return "/"
    else:
        path = "/" + "/".join(result)

        return path
