def simplify_path(path: str) -> str:
    path = path[1::].split("/")
    result = []
    for elem in path:
        match elem:
            case "..":
                if not result:
                    return ""
                result.pop()
                continue

            case ".":
                continue

            case "":
                continue

            case _:
                result.append(elem)

    return "/" + "/".join(result)
