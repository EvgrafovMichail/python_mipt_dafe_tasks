def int_to_roman(num: int) -> str:
    res = str()
    number = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    amount = 0
    while num > 0:
        if num >= 1000:
            amount = num // 1000
            place = 1000
        elif num >= 100:
            amount = num // 100
            place = 100
        elif num >= 10:
            amount = num // 10
            place = 10
        else:
            amount = num
            place = 1
        if amount == 9:
            res += number[place] + number[place * 10]
            num -= 9 * place
        elif amount == 4:
            res += number[place] + number[place * 5]
            num -= 4 * place
        elif (amount - 5) >= 0:
            res += number[place * 5]
            res += number[place] * (amount - 5)
            num -= amount * place
        else:
            res += number[place] * amount
            num -= amount * place
    return res
