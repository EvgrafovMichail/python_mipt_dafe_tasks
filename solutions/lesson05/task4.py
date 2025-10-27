def unzip(compress_text: str) -> str:
    strings = compress_text.split()
    compress_text = ""
    for elem in strings:
        if "*" in elem:
            string, mult = elem.split("*")
            compress_text += string * int(mult)
        else:
            compress_text += elem
    return compress_text
