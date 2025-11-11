def unzip(compress_text: str) -> str:
    output = ""
    for token in compress_text.split():
        if "*" in token:
            text, num = token.split("*")
            output += text * int(num)
        else:
            output += token
    return output
