def count_unique_words(text: str) -> int:
    # ваш код
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(",", "")
    text = text.split()
    dec_text = set()
    for i in text:
        if i not in dec_text:
            dec_text.add(i)
    return len(dec_text)
