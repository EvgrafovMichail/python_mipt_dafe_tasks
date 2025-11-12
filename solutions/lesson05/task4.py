def unzip(compress_text: str) -> str:
    tokens: list[str] = compress_text.replace("*", " ").split()

    result: str = ""

    for i in range(0, len(tokens)):
        if all([char.isdigit() for char in tokens[i]]) and i > 0:
            result += tokens[i - 1] * (int(tokens[i]) - 1)
        else:
            result += tokens[i]

    return result
