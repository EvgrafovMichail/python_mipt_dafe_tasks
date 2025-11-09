def simplify_path(path: str) -> str:
    parts = (path.replace("/", " ")).split()
    new_path = ""
    if len(path) == 0:
        return new_path
    elif ".." in parts:
        if (
            parts.count("..") > len(parts) - parts.count("..") - parts.count(".")
            or parts[0] == ".."
        ):
            return new_path
    new_path = [""]
    if len(parts) == 0:
        return "/"
    for elem in parts:
        if elem == ".":
            pass
        elif elem != "..":
            new_path.append(elem)
        elif elem == "..":
            new_path.pop()
    new_path = "/".join(new_path)
    if len(new_path) == 0:
        new_path = "/"
    return new_path
