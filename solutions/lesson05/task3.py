def is_punctuation(text: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet + alphabet.upper() + " " + "1234567890"
    exteption = list(alphabet)
    if text != "":
        for i in range(len(list(text))):
            if text[i] in exteption:
                return False
    else:
        return False
    return True
