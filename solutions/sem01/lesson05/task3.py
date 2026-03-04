def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False
    for char in text:
        if char not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            return False
    return True
