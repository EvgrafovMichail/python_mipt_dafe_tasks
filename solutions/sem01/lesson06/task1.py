def int_to_roman(num: int) -> str:
    roman_numbers = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    roman_digits = [1000, 500, 100, 50, 10, 5, 1]
    index = 0
    result = ""
    flag_close = False
    while index < len(roman_digits) and num > 0:
        if not flag_close and (num - roman_digits[index]) < 0:
            flag_close = True
        elif not flag_close:
            result += roman_numbers[roman_digits[index]]
            num -= roman_digits[index]
        elif flag_close:
            if (index == 0 or index == 2 or index == 4) and (
                num - (roman_digits[index] - 10 ** ((str(roman_digits[index]).count("0")) - 1))
            ) >= 0:
                num -= roman_digits[index] - 10 ** ((str(roman_digits[index]).count("0")) - 1)
                result += (
                    roman_numbers[10 ** ((str(roman_digits[index]).count("0")) - 1)]
                    + roman_numbers[roman_digits[index]]
                )
                flag_close = False
                index += 1
            elif (
                index != 2
                and index != 0
                and index != 4
                and (num - (roman_digits[index] - 10 ** str(roman_digits[index]).count("0"))) >= 0
            ):
                print(10 ** str(roman_digits[index]).count("0"))
                result += (
                    roman_numbers[10 ** str(roman_digits[index]).count("0")]
                    + roman_numbers[roman_digits[index]]
                )
                num -= roman_digits[index] - 10 ** str(roman_digits[index]).count("0")
                flag_close = False
                index += 1
            else:
                flag_close = False
                index += 1
    return result
