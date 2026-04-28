def are_anagrams(word1: str, word2: str) -> bool:
    n = len(word1)
    m = len(word2)

    if n != m:
        return False
    ascii_counter = [0] * 128
    for char in word1:
        ascii_counter[ord(char)] += 1
    for char in word2:
        ascii_counter[ord(char)] -= 1

    for symbol_count in ascii_counter:
        if symbol_count != 0:
            return False
    return True
