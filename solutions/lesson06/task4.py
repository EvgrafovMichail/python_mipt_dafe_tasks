def count_unique_words(text: str) -> int:
    final_unique_words = set()
    words = text.split()
    for word in words:
        start = 0
        while start < len(word) and not word[start].isalnum():
            start += 1
        end = len(word) - 1
        while end >= start and not word[end].isalnum():
            end -= 1
        if start <= end:
            cleaned_word = word[start : end + 1]
            standardized_word = cleaned_word.lower()

            final_unique_words = final_unique_words.union({standardized_word})
    return len(final_unique_words)
