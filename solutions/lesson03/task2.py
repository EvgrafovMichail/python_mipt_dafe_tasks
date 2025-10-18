def get_cube_root(n: float, eps: float) -> float:
    # Обработка нуля
    if n == 0:
        return 0.0

    # Определяем начальные границы поиска в зависимости от знака и величины n
    if n > 0:
        if n < 1:
            # Для чисел от 0 до 1 корень будет больше самого числа
            left = 0.0
            right = 1.0
        else:
            # Для чисел >= 1 корень будет не больше самого числа
            left = 0.0
            right = max(1.0, n)
    else:  # n < 0
        if n > -1:
            # Для чисел от -1 до 0 корень будет меньше самого числа
            left = -1.0
            right = 0.0
        else:
            # Для чисел <= -1 корень будет не меньше самого числа
            left = min(-1.0, n)
            right = 0.0

    # Бинарный поиск
    while abs(right - left) > eps:
        mid = (left + right) / 2
        mid_cubed = mid * mid * mid

        if mid_cubed < n:
            left = mid
        else:
            right = mid

    # Возвращаем среднее значение как приближение корня
    return (left + right) / 2


# print(get_cube_root(float(input("n = ")), float(input("eps = "))))
