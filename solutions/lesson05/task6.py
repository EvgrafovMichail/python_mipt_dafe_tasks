def simplify_path(path: str) -> str:
    lst = path.split("/")
    lst = [x for x in lst if x != "" and x != "."]

    i = 0
    while i < len(lst):
        if lst[i] == "..":
            if i <= 0:
                return ""
            else:
                lst.pop(i)
                lst.pop(i - 1)
                i -= 2
        elif lst[i] == ".":
            lst.pop(i)
            i -= 1

        i += 1
    path = "/" + "/".join(lst)
    return path
