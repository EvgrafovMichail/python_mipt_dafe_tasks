def count_unique_words(text: str) -> int:
    for i in ',.?!;:':
        text = text.replace(i, '')
    return len(set(text.lower().split()))