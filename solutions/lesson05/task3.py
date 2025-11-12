def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False
    else:
        for i in range(0, len(text)):
            if not (
                (ord(text[i]) >= 33 and ord(text[i]) <= 47)
                or (ord(text[i]) >= 58 and ord(text[i]) <= 64)
                or (ord(text[i]) >= 91 and ord(text[i]) <= 96)
                or (ord(text[i]) >= 123 and ord(text[i]) <= 126)
            ):
                return False
    return True


# 33-47
# 58-64
# 91-96
# 123-126
