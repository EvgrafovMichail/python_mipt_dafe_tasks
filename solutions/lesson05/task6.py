def simplify_path(path: str) -> str:
    path += "/"
    record = ""
    status = 0
    simple_path = "/"
    for i in path[1:]:
        if i == "/":
            if status == 1:
                status = 0

                if record == "..":
                    simple_path = simple_path[:-1]
                    if simple_path == "":
                        return simple_path
                    for j in range(len(simple_path) - 1, -1, -1):
                        if simple_path[j] == "/":
                            simple_path = simple_path[:j]
                            break

                elif record != ".":
                    simple_path += record
                if record != "" and record != ".":
                    simple_path += "/"

                record = ""
        elif status == 1:
            record += i
        else:
            status = 1
            record += i
    if simple_path != "/":
        return simple_path[:-1]
    return simple_path
