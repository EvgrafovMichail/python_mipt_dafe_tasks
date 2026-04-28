def simplify_path(path: str) -> str:
    catalogs = path.split("/")

    while "" in catalogs:
        catalogs.remove("")

    while "." in catalogs:
        catalogs.remove(".")

    while ".." in catalogs:
        index = catalogs.index("..")
        if index == 0:
            return ""
        catalogs.remove(catalogs[index])
        catalogs.remove(catalogs[index - 1])

    path = ""
    if catalogs != []:
        for catalog in catalogs:
            path += "/" + catalog
    else:
        path += "/"

    return path
