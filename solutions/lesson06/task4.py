def count_unique_words(text: str) -> int:
    if len(text) == 0:
        return 0
    text = text.lower()
    words = []
    current_word = ""
    for i in range(0, len(text)):
        if text[i].isalnum():
            current_word += text[i]
        if text[i] == " " and current_word != "":
            if current_word not in words:
                words.append(current_word)
                current_word = ""
            else:
                current_word = ""
    if current_word not in words and current_word != "":
        words.append(current_word)
    return len(words)
