def is_punctuation(text: str) -> bool:
    alphabet1 = '!"#$%&'
    alphabet2 = "'()*+,-./:;<=>?@[\]^_{|}~`"
    i = 10
    for i in text:
        if i not in alphabet2 and i not in alphabet1:
            return False
    if i == 10:
        return False
    return True
