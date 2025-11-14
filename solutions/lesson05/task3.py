def is_punctuation(text: str) -> bool:
    alf = """ !"#$%&'()*+,-./:;<=>?@[\]^_{|}~` """
    if text == "":
        return False
    if " " in text:
        return False
    for i in text:
        if i not in alf:
            return False
    return True
