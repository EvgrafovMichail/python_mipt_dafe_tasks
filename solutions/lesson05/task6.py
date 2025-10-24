def simplify_path(path: str) -> str:
    current_path = []
    for part in path.split("/"):
        if part == "..":
            if current_path:
                current_path.pop()
            else:
                return ""
        elif part == "." or part == "":
            continue
        else:
            current_path.append(part)
    return ("/" + "/".join(current_path)) if current_path else "/"
