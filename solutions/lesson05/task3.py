def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False
    for i in text:
        j = ord(i)
        if not (33 <= j <= 47 or 58 <= j <= 64 or 91 <= j <= 96 or 123 <= j <= 126):
            return False
    return True
