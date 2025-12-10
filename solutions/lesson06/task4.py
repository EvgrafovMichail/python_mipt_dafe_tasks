def count_unique_words(text: str) -> int:
    unique_words = set()
    buffer = ""

    for char in text:
        if char.isalnum() or char == "'":
            buffer += char.upper()
            continue

        if buffer:
            unique_words.add(buffer)
            buffer = ""

    if buffer:
        unique_words.add(buffer)

    return len(unique_words)
