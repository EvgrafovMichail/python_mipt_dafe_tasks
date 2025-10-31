import string


def count_unique_words(text: str) -> int:
    text = text.lower()
    words = text.split(" ")
    unique_words = set()
    for i in range(len(words)):
        word = words[i].strip(string.punctuation)
        if word or any(letter.isalnum() for letter in word):
            unique_words.add(word)
    return len(unique_words)
