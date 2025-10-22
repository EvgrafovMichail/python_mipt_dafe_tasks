def is_punctuation(text: str) -> bool:
    punct = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"

    if not text:
        return 0

    for i in text:
        if i not in punct:
            return 0
    return 1
