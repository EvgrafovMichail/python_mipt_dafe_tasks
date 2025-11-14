from string import punctuation


def count_unique_words(text: str) -> int:
    ans = []
    text = text.split(" ")
    for w in text:
        w = (w.lower()).strip(punctuation)
        if len(w):
            ans.append(w)
    return len(set(ans))
