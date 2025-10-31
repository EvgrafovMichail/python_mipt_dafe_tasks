def int_to_roman(num: int) -> str:
    roman = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    ans = ""
    for key in roman:
        while num >= roman[key]:
            num -= roman[key]
            ans += key
    return ans


print(int_to_roman(454))
