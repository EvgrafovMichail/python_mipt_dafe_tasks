def unzip(compress_text: str) -> str:
    text_list = compress_text.split()
    text = ""
    for i in range(len(text_list)):
        if "*" in text_list[i]:
            t = text_list[i].split("*")
            text_list[i] = t[0] * int(t[1])
        text += text_list[i]
    return text