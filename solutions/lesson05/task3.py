def is_punctuation(text: str) -> bool:
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"

    if text == "":
        return False

    for i in text:
        if i not in symbols:
            return False

    return True


print(is_punctuation('!"#$'))
