def simplify_path(path: str) -> str:
    # ваш код
    els = path.split("/")
    list = []
    for el in els:
        if el == "" or el == ".":
            continue
        elif el == "..":
            if len(list) != 0:
                list.pop()
            else:
                return ""
        else:
            list.append(el)
    path = "/" + "/".join(list)
    return path
