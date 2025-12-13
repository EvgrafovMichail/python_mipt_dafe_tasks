def simplify_path(path: str) -> str:
    path += "/"  # чтобы некст цикл адекватно работал
    while "//" in path or "/./" in path:
        path = path.replace("//", "/")  # избавился от лишних слэшей
        path = path.replace("/./", "/")  # так как она возвращает в этот же каталог, она бесполезна
    p = path.split("/")[1:]  # срез потому что на нулевом индексу пустая строка будет
    if path == "/":
        return path
    newpath = []
    level = 0  # для подсчета на каком мы щас "уровне", чтоб .. не вылетала
    for i in p:
        if i == "..":
            if level == 0:
                return ""
            else:
                level -= 1
                newpath.pop(-1)
        else:
            newpath.append(i)
            level += 1
    if len(newpath) == 0:
        return "/"
    return "/" + "/".join(newpath)[:-1]
