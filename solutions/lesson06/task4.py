def count_unique_words(text: str) -> int:
    words = text.split()
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    new_words = []
    for word in words:
        for elem in punctuation:
            word = word.replace(elem, "")
        if word:
            new_words.append(word.lower())
    return len(set(new_words))


