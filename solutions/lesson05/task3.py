def is_punctuation(text: str) -> bool:
    a = "!'"
    b = '#$%&"()*+,-./:;<=>?@[\]^_{|}~`'
    if len(text) != 0:
        for symbol in text:
            if symbol not in a + b:
                return False
        return True
    return False
