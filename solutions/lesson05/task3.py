def is_punctuation(text: str) -> bool:
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
    if len(text) == 0:
        return False
    for i in text:
        if i not in punctuation:
            return False
    return True
