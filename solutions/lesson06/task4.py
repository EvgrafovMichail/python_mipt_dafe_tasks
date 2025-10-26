def count_unique_words(text: str) -> int:
    text = text.lower()

    set_of_substr = set()
    sub_str = ""
    for symb in text:
        if symb.isalpha() or symb.isdigit() or (symb == "'"):
            sub_str += symb
        else:
            if sub_str != "":
                set_of_substr.add(sub_str)
                sub_str = ""

    if sub_str != "":
        set_of_substr.add(sub_str)

    return len(set_of_substr)
