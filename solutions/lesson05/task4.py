def unzip(compress_text: str) -> str:
    text = ""
    substr = [x.split("*") for x in compress_text.split(" ")]
    for x in substr:
        if len(x) == 1:
            text += x[0]
        else:
            text += x[0] * int(x[1])
    return text
