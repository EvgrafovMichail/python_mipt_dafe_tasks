def count_unique_words(text: str) -> int:
    if not text or text.isspace():
        return 0

    words = text.split()

    punctuation = '.,!?;:"()[]{}«»‹›<>„“”‘’‛′″‴‐‑–—―~`@#$%^&*_+=|\\/'
    cleaned_words = []

    for word in words:
        cleaned_word = word.strip(punctuation)

        if cleaned_word:
            cleaned_words.append(cleaned_word.upper())

    unique_words = set(cleaned_words)
    return len(unique_words)
