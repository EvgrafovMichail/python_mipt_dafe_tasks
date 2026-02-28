def count_unique_words(text: str) -> int:
    if len(text) == 0:
        return 0
    text = text.lower()
    for i in text:
        if i.isalpha() or i == " " or i.isdigit():
            continue
        else:
            text = text.replace(i, "")
    res = set(text.split())
    return len(res)
