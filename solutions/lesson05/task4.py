def unzip(compress_text: str) -> str:
    d = ""
    for i in compress_text.split():
        if "*" in i:
            b = i.split("*")
            d += b[0] * int(b[1])
        else:
            d += i
    return d
