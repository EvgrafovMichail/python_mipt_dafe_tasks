def is_punctuation(text: str) -> bool:
    if not text:
        return False

    punctuation = set(r"""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`""")

    for ch in text:
        if ch not in punctuation:
            return False
    return True
