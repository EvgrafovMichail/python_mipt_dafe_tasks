def count_unique_words(text: str) -> int:
    text = text.lower()
    words = text.split(" ")
    count_word = {}
    punctuation_marks = "!#$%&'()*+,-./:;<=>?@[\]^_{|}~`\""
    for word in words:
        while word and word[0]  in punctuation_marks:
            word = word[1:]
        while word and word[-1]  in punctuation_marks:
            word = word[:-1]
        if word:
            count_word[word] = count_word.get(word, 0)+1
    return len(count_word)
