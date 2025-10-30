def count_unique_words(s: str) -> int:
    import string

    s = s.split()

    unique_words = set()

    for word in s:
        word = word.lower().strip(string.punctuation)
        if word != '':
            unique_words.add(word)

    return len(unique_words)