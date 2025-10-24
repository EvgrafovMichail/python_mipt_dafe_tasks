def simplify_path(path: str) -> str:
    sub_path = path.split("/")
    way = []

    for i in sub_path:
        if i == "" or i == ".":
            continue
        if i == "..":
            if len(way) > 0:
                way.pop()
            else:
                return ""
            continue
        way.append(i)
    if not way:
        return "/"

    res = "/" + "/".join(way)
    return res
