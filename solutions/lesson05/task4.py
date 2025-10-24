def unzip(compress_text: str) -> str:
    text = []
    str = compress_text.split()
    if "*" in str:
        podstr, n = str.split("*")
        n = int(n)
        text.append(podstr * n)
    else:
        text.append(str)

    return "".join(text)
