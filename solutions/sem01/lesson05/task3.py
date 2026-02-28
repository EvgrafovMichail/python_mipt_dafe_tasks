def is_punctuation(text: str) -> bool:
    if not text:
        return False
    for i in text:
        if i not in r'!"#$%&\'()*+,-./:;<=>?@[]^_{|}~`':
            return False
    return True
