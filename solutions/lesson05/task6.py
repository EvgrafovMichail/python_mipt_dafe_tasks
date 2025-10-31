def simplify_path(path: str) -> str:
    # разделять строку по символам / и потом пустые строки удалять, точки заменять и все скреплять через матч кейс
    # чситка списка
    list = path.split("/")
    i = 0
    while i < len(list):
        match list[i]:
            case "" | ".":
                list.pop(i)
            case "..":
                if i == 0:
                    return ""
                else:
                    list.pop(i)
                    list.pop(i - 1)
                    i -= 1
            case _:
                i += 1

    # блок сборки строки

    final = ""
    for i in range(len(list)):
        final = final + "/" + list[i]

    # если в итоге мы ничего не сделали и остались в той же дирректории то вернем "/"
    if final == "":
        final = "/"
    return final
