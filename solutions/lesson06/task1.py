def int_to_roman(num: int) -> str:
    numbers = {
        "1000": "M",
        "900": "CM",
        "500": "D",
        "400": "CD",
        "100": "C",
        "90": "XC",
        "50": "L",
        "40": "XL",
        "10": "X",
        "9": "IX",
        "5": "V",
        "4": "IV",
        "1": "I",
    }
    result = ""
    for value in numbers.keys():
        while num >= int(value):
            result += numbers[value]
            num -= int(value)
    return result


print(int_to_roman(77))
