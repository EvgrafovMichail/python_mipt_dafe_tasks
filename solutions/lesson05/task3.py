import string


def is_punctuation(text: str) -> bool:
    punctuation = list(string.punctuation)
    lst_clear = text

    if len(text) == 0:
        return False

    for element in punctuation:
        lst_clear = lst_clear.replace(element, "")

    return lst_clear == ""
