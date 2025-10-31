def is_punctuation(text: str) -> bool:
    if not text:
        return False

    dic = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""
    for ch in text:
        if ch not in dic:
            return False
    return True


# print(is_punctuation(input()))
