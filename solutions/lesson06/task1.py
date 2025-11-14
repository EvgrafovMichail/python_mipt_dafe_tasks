def int_to_roman(num: int) -> str:
    result = ""
    reference = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    reverse = dict((key, val) for val, key in reference.items())
    values = [1000, 500, 100, 50, 10, 1]

    for val in values:
        while num >= val:
            if val == 1 or val == 10 or val == 100:
                variant = []

                if val * 10 in values:
                    variant.append(val * 10)

                if val * 5 in reference.values():
                    variant.append(val * 5)

                for prev in variant:
                    if num >= prev - val:
                        result += reverse[val] + reverse[prev]
                        num -= prev - val
                        break

                else:
                    result += reverse[val]
                    num -= val

            else:
                result += reverse[val]
                num -= val

    return result
