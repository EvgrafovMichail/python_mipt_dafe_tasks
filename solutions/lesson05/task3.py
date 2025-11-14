def is_punctuation(text: str) -> bool:
    if not text:
        return False
    chars = "!" + '"' + "#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
    fl = True
    for char in text:
        if char not in chars:
            fl = False
    return fl
