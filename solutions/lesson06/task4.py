def count_unique_words(text: str) -> int:
    charsprep = [",", ".", "!", "?", ":", ";", '"', "/", "-"]
    text = text.lower()

    for char in charsprep:
        text = text.replace(char, "")

    text = text.split()
    text = [word for word in text if word]

    return len(set(list(text)))
