def simplify_path(path: str) -> str:
    path = path.split("/")
    queue = []
    for dir in path:
        if dir == "" or dir == ".":
            continue
        elif dir == "..":
            if queue:
                queue.pop()
            else:
                return ""
        else:
            queue.append(dir)
    final_path = "/" + "/".join(queue)

    return final_path
