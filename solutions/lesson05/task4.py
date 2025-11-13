def unzip(compress_text: str) -> str:
    lst = compress_text.split(" ")
    unzip_lst = []
    for i in lst:
        s = i.split("*")
        if len(s) > 1:
            unzip_lst.append(s[0] * int(s[1]))
        else:
            unzip_lst.append(s[0])

    unzip_text = ""

    for i in unzip_lst:
        unzip_text += i

    return unzip_text


# print(unzip("AbcD*4 ef GhI*2"))
