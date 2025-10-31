import string


def count_unique_words(text: str) -> int:
    text = text.lower()
    words = text.split()
    unique = set()
    for word in words:
        while word and word[0] in string.punctuation:
            word = word[1:]

        while word and word[-1] in string.punctuation:
            word = word[:-1]

        if word:
            unique.add(word)

    return len(unique)


# print(count_unique_words(input()))
