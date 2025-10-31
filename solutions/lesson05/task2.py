def are_anagrams(w1: str, w2: str) -> bool:
    if len(w1) != len(w2):
        return False
    alphs = [0] * 123
    for char in w1:
        alphs[ord(char)] += 1
    for char in w2:
        alphs[ord(char)] -= 1
    fl = True
    for char in alphs:
        if char != 0:
            fl = False
            break
    return fl
