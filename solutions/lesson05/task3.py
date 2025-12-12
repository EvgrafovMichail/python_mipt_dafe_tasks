def is_punctuation(text: str) -> bool:
    symbols = '!"#$%&' + "'()*+,-./:;<=>?@[\]^_{|}~`"
    if text == "":
        return False
    for x in text:
        if x not in symbols:
            return False
    return True
