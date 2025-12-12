def is_punctuation(text: str) -> bool:
    if text == "":
        return False
    puncts = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"

    for i in text:
        if i not in puncts:
            return False
    return True
