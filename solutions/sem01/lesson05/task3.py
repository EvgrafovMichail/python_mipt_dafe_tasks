def is_punctuation(s):
    if len(s) == 0:
        return False

    punctuation = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    for char in s:
        if char not in punctuation:
            return False
    return True
