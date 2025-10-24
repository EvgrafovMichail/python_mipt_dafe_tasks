def unzip(compress_text: str) -> str:
    result = ""
    parts = compress_text.split()

    for part in parts:
        if "*" in part:
            text, number_str = part.split("*", 1)
            result += text * int(number_str)
        else:
            result += part

    return result
