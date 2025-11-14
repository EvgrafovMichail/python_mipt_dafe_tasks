def count_unique_words(text: str) -> int:
    words = text.split()
    d = {}
    i = 0
    for word in words:
        word = word.lower()
        while word:
            if not (
                65 <= ord(word[0]) <= 90 or 97 <= ord(word[0]) <= 122 or 48 <= ord(word[0]) <= 57
            ):
                word = word[1:]
            else:
                break
        while word:
            if not (
                65 <= ord(word[-1]) <= 90 or 97 <= ord(word[-1]) <= 122 or 48 <= ord(word[-1]) <= 57
            ):
                word = word[:-1]
            else:
                break
        if word not in d and word:
            i += 1
            d[word] = int()
    return i
