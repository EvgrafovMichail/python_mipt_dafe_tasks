def is_punctuation(text: str) -> bool:
    alphabet = "!""#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
    if text == "":
        return False
    for sym in text:
        if sym not in alphabet:
            return False
    return True
