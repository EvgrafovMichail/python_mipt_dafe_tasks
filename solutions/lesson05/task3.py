def is_punctuation(text: str) -> bool:
    c = 0
    zn_p = '!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~`'
    for i in text:
        if i in zn_p:
            c += 1
    if c == len(text) and len(text) != 0:
        return True
    return False
