def paw_ten(n: int):
    ans = 1
    i = 0
    while i < n:
        ans = ans * 10
        i += 1
    return ans


def is_palindrome(num: int) -> bool:
    if num < 0:
        return False

    num_reversed = 0
    num_origin = num
    t = num_origin
    n = 0
    while t != 0:
        t = t // 10
        n += 1

    t = num_origin

    while n != 0:
        num_reversed = num_reversed + t % 10 * paw_ten(n - 1)
        t = t // 10
        n -= 1

    return num_origin == num_reversed


print(is_palindrome(-1))
