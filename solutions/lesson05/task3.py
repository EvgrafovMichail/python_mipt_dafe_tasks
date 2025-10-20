def is_punctuation(text: str) -> bool:
    # ваш код
    punctuation_symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
    if text == "":
        return False
    for i in range(len(text)):
        if text[i] in punctuation_symbols:
            continue
        else:
            return False
    return True
