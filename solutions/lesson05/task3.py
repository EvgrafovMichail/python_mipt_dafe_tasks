def is_punctuation(text: str) -> bool:
    if text == "":
        return False

    allowed_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
    for char in text:
        if char not in allowed_chars:
            return False
    return True
