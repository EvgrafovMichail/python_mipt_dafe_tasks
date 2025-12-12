def simplify_path(path: str) -> str:
    spisok = []
    podstr = path.split("/")

    for i in podstr:
        if i == "" or i == ".":
            continue
        elif i == "..":
            if spisok:
                spisok.pop()
            else:
                return ""
        else:
            spisok.append(i)
    result = "/" + "/".join(spisok)
    return result
