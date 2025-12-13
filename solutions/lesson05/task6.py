def simplify_path(path: str) -> str:
    parts = path.split("/")
    res = []
    i = 0
    while i < len(parts):
        part = parts[i]
        if not part or part == ".":
            i += 1
            continue
        if part == "..":
            if res:
                res.pop()
            else:
                return ""
        else:
            res.append(part)
        i += 1
    if not res:
        return "/"
    return "/" + "/".join(res)
