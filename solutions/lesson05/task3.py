def is_punctuation(text: str) -> bool:
    if text == "":
        return False
    for i in [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "'",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "]",
        "^",
        "_",
        "{",
        "|",
        "}",
        "~",
        "`",
        "\\",
    ]:
        text = text.replace(i, "")
    if text == "":
        return True
    return False
