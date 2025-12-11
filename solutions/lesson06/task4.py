def count_unique_words(text: str) -> int:
    # ваш код
    only_text = ""
    for char in text:
        if char.isalpha() or char.isdigit() or char.isspace():
            only_text += char.lower()

    result = set(only_text.split(" "))
    filtered_list = []
    for i in result:
        if i != "":
            filtered_list.append(i)

    return len(filtered_list)
