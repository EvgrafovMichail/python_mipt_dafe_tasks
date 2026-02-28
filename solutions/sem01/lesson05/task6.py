def simplify_path(path: str) -> str:
    catalogs = []
    for i in path.replace("//", "/").split("/"):
        if i == ".." and not catalogs:
            return ""
        if i == "..":
            del catalogs[-1]
            continue
        if i == ".":
            continue
        if i:
            catalogs.append(i)

    return "/" + "/".join(catalogs)
