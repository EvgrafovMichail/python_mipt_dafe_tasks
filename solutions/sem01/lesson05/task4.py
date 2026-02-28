def unzip(compress_text: str) -> str:
    result = ""
    for i in compress_text.split():
        if "*" in i:
            s, count = i.split("*")
            result += s * int(count)
        else:
            result += i
    return result
