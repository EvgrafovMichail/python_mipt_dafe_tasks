def unzip(compress_text: str) -> str:
    result = ""
    for part in compress_text.split():
        if "*" in part:
            substr, repeat_num = part.split("*")
            result += substr * int(repeat_num)
        else:
            result += part
    return result
