def are_anagrams(word1: str, word2: str) -> bool:
    chars_count = [0] * 123  # Индекс списка - номер символа в таблице ASCII

    for char in word1:
        chars_count[ord(char)] += 1

    for char in word2:
        chars_count[ord(char)] -= 1

    for elem in chars_count:
        if elem != 0:
            return False
    return True
