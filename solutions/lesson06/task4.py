import string


def count_unique_words(text: str) -> int:
    punctuation = string.punctuation

    set_of_words = set()

    for word in text.split():
        if word.strip(punctuation) and word.strip(punctuation).lower() not in set_of_words:
            set_of_words.add(word.strip(punctuation).lower())

    return len(set_of_words)
