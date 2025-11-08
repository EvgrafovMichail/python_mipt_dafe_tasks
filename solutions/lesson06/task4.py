import string


def count_unique_words(text: str) -> int:
    unique_words = set()

    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if word not in unique_words and word != "":
            unique_words.add(word)

    return len(unique_words)
