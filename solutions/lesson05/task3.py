def is_punctuation(text: str) -> bool:
    if not text:
        return False
    p = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
    for w in text:
        if w not in p:
            return False
    return True
