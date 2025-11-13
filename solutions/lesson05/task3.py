def is_punctuation(text: str) -> bool:
    if len(text)==0:
        return 0
    for i in range(len(text)):
        if not(text[i] in "!\"}#$%&'()*+,-./:;<=>?@[\]^_{|}~`"):
            return False
    return True
