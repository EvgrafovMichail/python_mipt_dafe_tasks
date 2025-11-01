def int_to_roman(num: int) -> str:
    rom_dict = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    res = []
    for value in values:
        while num >= value:
            result.append(rom_dict[value])
            num -= value
    return ''.join(res)
