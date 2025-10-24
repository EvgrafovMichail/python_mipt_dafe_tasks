def simplify_path(path: str) -> str:
    splitted_path = []
    for sub_str in path.split("/"):
        if (sub_str != "") and (sub_str != "."):
            splitted_path.append(sub_str)

    cleaned_path = []
    for dir in splitted_path:
        if dir != "..":
            cleaned_path.append(dir)
        else:
            if cleaned_path == []:
                return ""
            cleaned_path.pop()

    if cleaned_path == []:
        return "/"

    out_path = ""
    for name in cleaned_path:
        out_path += "/" + name
    return out_path
