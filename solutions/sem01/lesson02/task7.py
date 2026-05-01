def is_palindrome(num: int) -> bool:
    if num < 0:
        return False

    elif num < 10:
        return True

    else:
        num_copy = num
        category = 0
        while num_copy > 0:
            category += 1
            num_copy = num_copy // 10
        i = 0
        num_copy = num
        while i < category:
            if num_copy % (10) != (num // (10 ** (category - 1 - i))) % 10:
                return False
            else:
                i += 1
                num_copy //= 10
        return True
