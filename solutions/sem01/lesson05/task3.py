def is_punctuation(text: str) -> bool:
    if not text:
        return False
    punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""
    for symbol in text:
        if symbol not in punctuations:
            return False
    return True
