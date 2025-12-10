def is_punctuation(text: str) -> bool:
    if text == "":
        return False
    for i in text:
        if i.isalnum() or i.isspace():
            return False

    return True
