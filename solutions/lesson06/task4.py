def count_unique_words(text: str) -> int:
    text = text.lower()
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    return len(set(text.split()))

print(count_unique_words("word... word!!!"))


