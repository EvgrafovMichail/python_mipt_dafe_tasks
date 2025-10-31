def simplify_path(path: str) -> str:
    parts = path.split("/")
    stack = []
    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
            else:
                return ""
        else:
            stack.append(part)
    return "/" + "/".join(stack) if stack else "/"
