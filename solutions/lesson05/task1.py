def is_palindrome(text: str) -> bool:

    lst = list(text.lower())
    n = len(lst)

    if n == 0 or n == 1:
        return True
    
    for i in range(1, n // 2 + 1):
        if lst[i - 1] == lst[-i]:
            return True
        else:
            return False