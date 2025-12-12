def is_punctuation(text: str) -> bool:
    symbols = "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~`" + '"'
    if len(text) == 0:
        return False
    for elem in text:
        if elem not in symbols:
            return False
    return True
