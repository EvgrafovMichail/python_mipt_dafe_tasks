def is_punctuation(text: str) -> bool:
    if text == "":
        return False

    punct = """!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~"""

    for i in text:
        if i not in punct:
            return False

    return True
