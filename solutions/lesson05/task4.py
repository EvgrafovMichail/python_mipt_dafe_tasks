def unzip(compress_text: str) -> str:
    text = ""
    for token in compress_text.split():
        if "*" in token:
            word, count = token.split("*")
            text += word * int(count)
        else:
            text += token
    return text


print(unzip("a*3 b*2"))
