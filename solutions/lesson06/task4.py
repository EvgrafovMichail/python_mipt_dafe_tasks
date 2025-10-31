def count_unique_words(text: str) -> int:
    text2 = "".join([char for char in text if char.isalnum() or char == " "])
    text2 = text2.lower()
    split_str = text2.split(" ")
    split_str2 = []
    for i in split_str:
        if i != "":
            split_str2.append(i)

    s = set(split_str2)

    return len(s)
