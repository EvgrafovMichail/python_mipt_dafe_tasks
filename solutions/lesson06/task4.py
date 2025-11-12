import string


def count_unique_words(text: str) -> int:
    al = string.ascii_letters + string.digits
    word = ""
    uwords = []
    for i in text:
        if i in al or i == "'":
            word += i
        else:
            word = word.lower()
            if word not in uwords and len(word) > 0:
                uwords.append(word)
            word = ""
    word = word.lower()
    if word not in uwords and len(word) > 0:
        uwords.append(word)
    return len(uwords)
