def is_punctuation(text: str) -> bool:
    # ваш код
    if text == "":
        return False
    check = """!"#$%&'()*+,-./:;<=>?@[]\^_{|}~`"""
    for i in range(len(text)):
        if text[i] not in check:
            return False
    return True
