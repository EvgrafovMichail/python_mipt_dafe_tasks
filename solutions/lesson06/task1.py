def int_to_roman(num: int) -> str:
    dictionary = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    answer = ""
    while num > 0:
        for value in dictionary.keys():
            if num >= value:
                answer += dictionary[value]
                num -= value
                break
    return answer
