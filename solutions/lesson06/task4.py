def count_unique_words(text: str) -> int:
    words = text.split()
    seen = set()
    for i in words:
        i = i.strip("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
        i = i.lower()
        if i:
            seen.add(i)
    return len(seen)
