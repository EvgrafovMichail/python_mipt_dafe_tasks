def simplify_path(path: str) -> str:
    path.replace("//", "/")
    pathlist = path.split("/")
    if pathlist[0] == "":
        del pathlist[0]

    res_path = []
    counter = 0

    for i in pathlist:
        if i == ".":
            continue

        elif i == "..":
            if not (res_path):
                return ""
            else:
                counter -= 1
                del res_path[counter]

        else:
            if i != "":
                res_path.append(i)
                counter += 1

    if not (res_path):
        return "/"

    path = ""

    for i in res_path:
        path += "/" + i

    return path
