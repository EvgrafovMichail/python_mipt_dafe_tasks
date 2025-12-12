import string


def delete_punc(word):
    if not word:
        return ""
    N = len(word)
    i = 0
    j = len(word) - 1
    while i < N and word[i] in string.punctuation:
        i += 1
    while j >= i and word[j] in string.punctuation:
        j -= 1
    return word[i : j + 1]


def count_unique_words(text: str) -> int:
    word = ""
    unique = set()
    for i in text:
        if i != " ":
            word += i.lower()
        if i == " ":
            word = delete_punc(word)
            if word:
                unique.add(word.lower())
            word = ""
    if word:
        word = delete_punc(word)
        if word:
            unique.add(word.lower())

    return len(unique)


print(count_unique_words("???, ???, ???"))
