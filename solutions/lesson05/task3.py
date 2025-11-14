def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False

    need = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"

    for i in text:
        if i not in need:
            return False

    return True
