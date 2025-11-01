def count_unique_words(text: str) -> int:
    text = text.lower()
    res = ""
    for i in range(len(text)):
        if (text[i] >= 'a' and text[i] <= 'z') or (text[i] >= '0' and text[i] <= '9') or text[i] == " ":
            res += text[i]

    return len(set(res.split()))
