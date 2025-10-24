def simplify_path(path: str) -> str:
    if path[0] != "/":
        return ""

    newpath = ""
    slash = False
    for char in path:  # убираем лишние слэши
        if char == "/" and not slash:
            slash = True
            newpath += char
        elif char == "/" and slash:
            pass
        else:
            newpath += char
            slash = False

    if newpath[-1] == "/":
        newpath = newpath[:-1]

    listpath = newpath.split("/")[1:]
    path = []
    for i in range(len(listpath)):
        if (not path) and (listpath[i] == ".."):
            return ""
        elif listpath[i] == ".":
            pass
        elif listpath[i] == "..":
            path.pop(-1)
        else:
            path.append(listpath[i])

    respath = "/" + "/".join(path)

    return respath
