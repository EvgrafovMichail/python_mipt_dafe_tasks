def count_unique_words(text: str) -> int:
    words = set()
    word = ""

    for i in text:
        if i.isalnum() or i == "'":
            word += i.lower()
        else:
            words.add(word)
            word = ""

    words.add(word)

    return len(words) - (1 if "" in words else 0)
