def simplify_path(path: str) -> str:
    stack = []
    parts = [p for p in path.split("/") if p != "" and p != "."]
    for part in parts:
        if part == "..":
            if stack:
                stack.pop()
            else:
                return ""
        else:
            stack.append(part)

    return "/" + "/".join(stack)
