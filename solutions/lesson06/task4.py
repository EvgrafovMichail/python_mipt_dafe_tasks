def count_unique_words(text: str) -> int:
    text = text.replace("!", "").replace("?", "").replace(".", "").replace(",", "")
    text = text.lower()
    ans = set()
    for i in text.split():
        if i not in ans:
            ans.add(i)
    return len(ans)
