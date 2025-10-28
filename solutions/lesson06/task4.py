def count_unique_words(text: str) -> int:
    text = text.lower()
    punctuation_marks = "!\"#$%&()*+,-./:;<=>?@[]^_{|}~`'\\"
    for mark in punctuation_marks:
        text = text.replace(mark, "")
    words = text.split()
    dictionary = {}
    for word in words:
        dictionary[word] = 1
    return len(dictionary)
