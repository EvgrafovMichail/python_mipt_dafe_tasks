def simplify_path(path: str) -> str:
    new = ""
    for ch in path:
        if ch != "'" and ch != '"':
            new += ch
    new = new.split("/")
    while "." in new:
        ind = new.index(".")
        del new[ind]
    while "" in new:
        ind = new.index("")
        del new[ind]
    while ".." in new:
        ind = new.index("..")
        if ind != 0:
            del new[ind - 1]
            del new[ind - 1]
        else:
            return ""
    new = "/" + "/".join(new)
    return new


if __name__ == "__main__":
    print(simplify_path("/"))
