def count_unique_words(text: str) -> int:
    text = text.lower() + " "
    words = set()
    word = ""
    for symbol in text:
        if symbol.isalnum() or symbol == "'":
            word += symbol
        elif word != "":
            words.add(word)
            word = ""
    return len(words)
