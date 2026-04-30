def unzip(compress_text: str) -> str:
    words = compress_text.split()
    result = ""
    for word in words:
        spl = word.split("*")
        if len(spl) == 1:
            result += spl[0]
        else:
            result += spl[0] * int(spl[1])
    return result
