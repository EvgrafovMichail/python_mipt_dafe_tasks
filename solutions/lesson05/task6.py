def simplify_path(path: str) -> str:
    result_path = []
    for command in path.split("/"):
        if command == ".":
            continue
        if command == "..":
            if not result_path:
                return ""
            result_path.pop()
        elif command:
            result_path.append(command)
    return "/" + "/".join(result_path)
