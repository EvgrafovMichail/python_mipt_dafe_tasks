def is_punctuation(text: str) -> bool:
    text = list(text)
    a = r"!#$%&'()*+,-./:;<=>?@[\]^_{|}~`" + '"'
    a = list(a)
    if len(text) != 0:
        for i in range(0, len(text)):
            if text[i] in a:
                continue
            else:
                return False
        return True
    return False
