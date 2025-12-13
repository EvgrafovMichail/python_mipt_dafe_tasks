def simplify_path(path: str) -> str:
    # ваш код
    parts = path.split("/")
    stack = []

    for part in parts:
        if part == "" or part == ".":
            continue
        if part == "..":
            if stack:
                stack.pop()
            else:
                return ""
        else:
            stack.append(part)

    return "/" + "/".join(stack)
