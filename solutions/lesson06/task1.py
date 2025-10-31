def upper_bound(arr, value):
    begin, end = 0, len(arr) - 1

    while begin <= end:
        mid = (begin + end) // 2

        if arr[mid] > value:
            begin = mid + 1
        else:
            end = mid - 1

    return arr[begin]


def relaxing_nums(roman_values, result):
    for i in range(len(roman_values) - 2):
        high, mid, low = roman_values[i], roman_values[i + 1], roman_values[i + 2]

        result = result.replace(mid + low * 4, low + high)
        result = result.replace(low * 4, low + mid)

    return result


def int_to_roman(num: int) -> str:
    roman_number = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}

    roman_keys = [*roman_number.keys()]
    roman_values = [*roman_number.values()]

    result = ""

    while num > 0:
        lower = upper_bound(roman_keys, num)

        result += roman_number[lower]
        num -= lower

    return relaxing_nums(roman_values, result)


for j in range(100):
    for i in range(1, 4000):
        (int_to_roman(i))
