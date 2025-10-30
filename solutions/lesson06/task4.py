def count_unique_words(text: str) -> int:
    # ваш код
    seen = set()
    for raw in text.split():
        word = raw.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~").lower()
        if word:
            seen.add(word)
    return len(seen)
