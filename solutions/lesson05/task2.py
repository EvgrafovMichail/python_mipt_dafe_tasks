def are_anagrams(word1: str, word2: str) -> bool:
    arr = [0] * 123

    for i in word1:
        arr[ord(i)] += 1

    for i in word2:
        arr[ord(i)] -= 1

    for i in arr:
        if i != 0:
            return False

    return True
