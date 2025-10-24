def is_punctuation(text: str) -> bool:
    if text == "":
        return False

    for i in text:
        if i not in "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`":
            return False
    return True
