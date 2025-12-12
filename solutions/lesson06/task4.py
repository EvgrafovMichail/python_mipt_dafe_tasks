def count_unique_words(text: str) -> int:
    new_text = ""
    for char in text.lower():
        if char in ',.!?:;-()"' or ord(char) == 39:
            continue
        else:
            new_text += char
    return len(set(new_text.split()))
