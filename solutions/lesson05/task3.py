def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False

    punctuation_marks = "!\"#$%&()*+,-./:;<=>?@[]^_{|}~`'\\"
    binary = 0
    for punctuation_mark in punctuation_marks:
        binary += 1 << ord(punctuation_mark)

    for symbol in text:
        if binary & (1 << ord(symbol)) == 0:
            return False
    return True
