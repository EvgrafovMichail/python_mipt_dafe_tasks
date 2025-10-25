def is_punctuation(text: str) -> bool:
    if text == "":
        return False

    for symb in text:
        if (
            (33 <= ord(symb) <= 47)
            or (58 <= ord(symb) <= 64)
            or (91 <= ord(symb) <= 96)
            or (123 <= ord(symb) <= 126)
        ):
            pass
        else:
            return False
    return True
