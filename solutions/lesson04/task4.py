def move_zeros_to_end(lis: list[int]) -> list[int]:
    char = len(lis) - lis.count(0)

    while lis[:char].count(0):
        lis.append(lis.pop(lis.index(0)))

    return char
