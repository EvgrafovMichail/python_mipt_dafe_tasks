def is_punctuation(text: str) -> bool:
    if text != '' and set(text) <= set('!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~`'):
        return True
    return False
