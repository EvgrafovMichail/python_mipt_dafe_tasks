def count_unique_words(text: str) -> int:
    text = text.lower()
    allowed = "qwertyuiopasdfghjklzxcvbnm0123456789"
    text = text.split()
    words = []
    for elem in text:
        string = ""
        for char in elem:
            if char in allowed:
                string += char
        if len(string) > 0:
            words.append(string)
    return len(set(words))
