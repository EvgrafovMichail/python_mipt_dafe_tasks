def count_unique_words(text: str) -> int:
    if len(text) == 0:
        return 0

    textsp = text.split()
    if len(textsp) == 0:
        return 0

    words = set()
    ##можно было через strip(string.punctuation)
    for i in textsp:
        while len(i) > 0 and not i[0].isalnum() and i[0] != "'":
            i = i[1:]

        while len(i) > 0 and not i[-1].isalnum() and i[0] != "'":
            i = i[:-1]

        if len(i) > 0 and (i.isalnum() or "'" in i):
            i = i.lower()
            words.add(i)

    return len(words)
