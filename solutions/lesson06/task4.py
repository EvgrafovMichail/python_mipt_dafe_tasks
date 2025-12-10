def count_unique_words(text: str) -> int:
    text = text.lower()
    new_text = ""
    for i in range(len(text)):
        if text[i] in "qwertyuiopasdfghjklzxcvbnm0123456789 ":
            new_text += text[i]
    a=set(new_text.split())
    return len(a)