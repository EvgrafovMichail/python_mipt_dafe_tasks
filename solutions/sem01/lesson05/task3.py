def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False
    symbol_of_punctuation = '!"#$%&()*+,-./:;<=>?@[\]^_{|}~`'
    for char in text:
        if char not in symbol_of_punctuation and ord(char) != 39:
            return False
    return True
