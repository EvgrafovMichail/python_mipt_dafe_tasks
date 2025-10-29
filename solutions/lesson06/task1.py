def int_to_roman(num: int) -> str:
     roman = [ ("I", 1), ("IV", 4), ("V",5 ), ("IX", 9) ,("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
              ("CD", 400), ("D", 500), ("CM", 900) ,("M", 1000)]
    used_roman = reversed(roman)
    res = ""
    for symbol , digit in used_roman:
        while num >= digit:
            res += symbol
            num -= digit
   return res
