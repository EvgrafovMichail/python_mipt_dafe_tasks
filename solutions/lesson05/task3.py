def is_punctuation(text: str) -> bool:
    # ваш код
    punctuation = """!"#$%&'()*+,-./:;<=>?@[\\]^{|}~`"""
    if not text:
        return False
    for ch in text:
        if ch not in punctuation:
            return False
    return True
