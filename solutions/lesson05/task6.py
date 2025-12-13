def simplify_path(path: str) -> str:
    if len(path) > 0:
        if path[-1] != "/":
            path += "/"
    while "//" in path:
        path = path.replace("//", "/", 1)
    while "/./" in path:
        path = path.replace("/./", "/", 1)
    while "/../" in path:
        index = path.find("/../")
        lindex = path[:index].rfind("/")
        temp = ""
        if lindex != -1:
            temp += path[:lindex]
            temp += "/"
        else:
            return ""
        temp += path[index + 4 :]
        path = temp
    if len(path) > 1:
        if path[-1] == "/":
            path = path[:-1]
    return path
