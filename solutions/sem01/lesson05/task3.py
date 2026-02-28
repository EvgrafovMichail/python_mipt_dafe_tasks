def is_punctuation(text: str) -> bool:
    if text == "":
        return False
    str1 = '!"#$%&'
    str2 = "'()*+,-./:;<=>?@[\\]^_{|}~`"
    str = str1 + str2
    if all(i in str for i in text):
        return True
    else:
        return False
