def count_unique_words(text: str) -> int:
    text = text.lower()
    s = set()
    left = 0
    for r in range(len(text)):
        if not (text[r].isalnum() or text[r] == "'"):
            if left < r:
                s.add(text[left:r])
            left = r + 1
    if left < len(text):
        s.add(text[left:])
    return len(s)
