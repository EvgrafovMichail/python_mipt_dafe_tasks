def is_punctuation(text: str) -> bool:
    if not text:
        return False
    
    ##return not text.strip(string.punctuation)
    need = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"

    for i in text:
        if i not in need:
            return False

    return True
