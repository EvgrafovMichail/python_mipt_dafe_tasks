def count_unique_words(text: str) -> int:
    text = (text.replace("!", " ").replace("?", " ").replace(",", " ").replace(".", " ")).lower()
    words = set(text.split())

    return len(words)
