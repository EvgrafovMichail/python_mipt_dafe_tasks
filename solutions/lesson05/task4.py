def unzip(compress_text: str) -> str:
    text = ""
    while compress_text:
        podstr = ""
        c = len(compress_text)
        for i in compress_text:
            if i == " ":
                c = compress_text.index(i)
                break
            else:
                podstr += i

        if "*" in podstr:
            text += podstr[: podstr.index("*")] * int(podstr[(podstr.index("*") + 1) :])
        else:
            text += podstr
        if c < len(compress_text):
            compress_text = compress_text[c + 1 :]
        else:
            compress_text = ""

    return text
