def count_unique_words(text: str) -> int:
    puncts = "!?.,;:-'\\()[]{}\"<>/"
    for i in puncts:
        text = text.replace(i, "")
    text = text.lower()
    words = set(text.split())
    return len(words)
