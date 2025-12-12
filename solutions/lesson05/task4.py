def unzip(compress_text: str) -> str:
    result = ""
    compress_text = compress_text.split(" ")
    for i in compress_text:
        if "*" not in i:
            result += i
        else:
            result += i[: i.find("*")] * int(i[i.find("*") + 1 :])
    return result
