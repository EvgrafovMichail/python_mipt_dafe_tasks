def simplify_path(path: str) -> str:
    if len(path) > 0 and path[len(path) - 1] == "/":
        path = path[:-1]

    spl = path.split("/")
    count = []

    i = len(spl) - 1
    curr = 0

    while i >= 0:
        if spl[i] == "" or spl[i] == ".":
            i -= 1

        elif spl[i] == "..":
            curr += 1
            i -= 1

        else:
            if curr > 0:
                curr -= 1
                i -= 1
            else:
                count.append(spl[i])
                i -= 1

    if curr > 0:
        return ""

    string = ""

    for i in range(len(count) - 1, -1, -1):
        string = string + "/" + count[i]

    if string == "":
        return "/"

    return string
