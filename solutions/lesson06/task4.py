def count_unique_words(text: str) -> int:
    lower_text = text.lower()
    words = lower_text.split()
    ans = set()
    s = ".,!?"
    for i in words:
        unique_words = i.strip(s)
        if unique_words:
            ans.add(unique_words)
    return len(ans)
