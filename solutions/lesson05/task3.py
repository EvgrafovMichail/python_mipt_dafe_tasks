def is_punctuation(text: str) -> bool:
    if not text:
        return False

    for i in text:
        if not i in "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`":
            return False

    return True
