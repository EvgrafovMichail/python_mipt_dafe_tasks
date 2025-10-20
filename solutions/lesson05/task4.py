def unzip(compress_text: str) -> str:
    compress_text = compress_text.split()
    string = ""
    for i in range(0, len(compress_text)):
        if "*" in compress_text[i]:
            string += compress_text[i].split("*")[0] * int(compress_text[i].split("*")[1])
        else:
            string += compress_text[i]
    return string
