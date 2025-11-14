def is_punctuation(text: str) -> bool:
    zn = r'!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~`'
    if not text:
        return False
    for ch in text:
        if ch not in zn:
            return False
    return True


if __name__ == "__main__":
    print(is_punctuation(""))
