def reg_validator(reg_expr: str, text: str) -> bool:
    reg_expr_lst = reg_expr.split("-")
    text_lst = text.split("-")
    if len(reg_expr_lst) != len(text_lst):
        return False

    for i in range(len(text_lst)):
        a = reg_expr_lst[i]
        h = text_lst[i]
        k = 0
        for j in range(len(a)):
            b = a[j]
            if k >= len(h):
                return False
            if b == "d":
                if not h[k].isdigit():
                    return False
                else:
                    while k < len(h) and h[k].isdigit():
                        k += 1
            elif b == "w":
                if not h[k].isalpha():
                    return False
                else:
                    while k < len(h) and h[k].isalpha():
                        k += 1
            elif b == "s":
                if not h[k].isalnum():
                    return False
                else:
                    while k < len(h) and h[k].isalnum():
                        k += 1
            else:
                if h[k] != b:
                    return False
                else:
                    k += 1
        if k != len(h):
            return False
    return True
