def int_to_roman(num: int) -> str:
    roman_numeral_sets = [
        {1: "I", 5: "V", 10: "X"},
        {1: "X", 5: "L", 10: "C"},
        {1: "C", 5: "D", 10: "M"},
        {1: "M"},
    ]
    s_num = str(num)
    n = len(s_num)
    result = []
    for i in range(n):
        digit_symbol = s_num[i]
        digit = int(digit_symbol)
        segment = ""
        index = n - 1 - i
        if index == 3:
            if digit > 0:
                segment = roman_numeral_sets[index][1] * digit
        elif index < 3:
            current_num = roman_numeral_sets[index]
            one = current_num[1]
            five = current_num[5]
            ten = current_num[10]
            if 1 <= digit <= 3:
                segment = one * digit
            elif digit == 4:
                segment = one + five
            elif digit == 5:
                segment = five
            elif 6 <= digit <= 8:
                segment = five + one * (digit - 5)
            elif digit == 9:
                segment = one + ten
        result.append(segment)
    return "".join(result)
