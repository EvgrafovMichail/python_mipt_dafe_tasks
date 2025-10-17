def move_zeros_to_end(l: list[int]) -> list[int]:
    char = len(l) - l.count(0)
    while l[:char].count(0):
        l.append(l.pop(l.index(0)))
    return char
