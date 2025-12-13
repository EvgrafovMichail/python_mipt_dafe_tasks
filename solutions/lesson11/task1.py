import math


class Vector2D:
    # инициализация вектора
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    # свойство абсциссы
    @property
    def abscissa(self) -> float:
        return self._abscissa

    # свойство ординаты
    @property
    def ordinate(self) -> float:
        return self._ordinate

    # строковое представление для print()
    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    # равенство векторов
    def __eq__(self, other_vector: object) -> bool:
        if not isinstance(other_vector, Vector2D):
            return False
        return self._abscissa == other_vector._abscissa and self._ordinate == other_vector._ordinate

    # неравенство векторов
    def __ne__(self, other_vector: object) -> bool:
        return not self.__eq__(other_vector)

    # сравнение (меньше)
    def __lt__(self, other_vector: "Vector2D") -> bool:
        if self._abscissa < other_vector._abscissa:
            return True
        elif self._abscissa == other_vector._abscissa:
            return self._ordinate < other_vector._ordinate
        return False

    # сравнение (меньше или равно)
    def __le__(self, other_vector: "Vector2D") -> bool:
        return self.__lt__(other_vector) or self.__eq__(other_vector)

    # сравнение (больше)
    def __gt__(self, other_vector: "Vector2D") -> bool:
        return not self.__le__(other_vector)

    # сравнение (больше или равно)
    def __ge__(self, other_vector: "Vector2D") -> bool:
        return not self.__lt__(other_vector)

    # вычисление длины вектора
    def __abs__(self) -> float:
        return (self._abscissa**2 + self._ordinate**2) ** 0.5

    # преобразование в логический тип
    def __bool__(self) -> bool:
        return abs(self) != 0.0

    # умножение вектора на число справа
    def __mul__(self, scalar_value: float) -> "Vector2D":
        return Vector2D(self._abscissa * scalar_value, self._ordinate * scalar_value)

    # умножение вектора на число слева
    def __rmul__(self, scalar_value: float) -> "Vector2D":
        return self.__mul__(scalar_value)

    # деление вектора на число (умножение на обратное)
    def __truediv__(self, scalar_value: float) -> "Vector2D":
        if scalar_value == 0:
            raise ZeroDivisionError("На ноль нельзя делить")
        return Vector2D(self._abscissa / scalar_value, self._ordinate / scalar_value)

    # сложение векторов и вектора с числом
    def __add__(self, addend) -> "Vector2D":
        if isinstance(addend, (int, float)):
            return Vector2D(self._abscissa + addend, self._ordinate + addend)
        elif isinstance(addend, Vector2D):
            return Vector2D(self._abscissa + addend._abscissa, self._ordinate + addend._ordinate)
        else:
            raise TypeError(f"Нельзя сложить Vector2D")

    # сложение числа с вектором слева
    def __radd__(self, addend: float) -> "Vector2D":
        return self.__add__(addend)

    # вычитание числа из вектора и вычитание векторов
    def __sub__(self, subtrahend) -> "Vector2D":
        if isinstance(subtrahend, (int, float)):
            return Vector2D(self._abscissa - subtrahend, self._ordinate - subtrahend)
        elif isinstance(subtrahend, Vector2D):
            return Vector2D(
                self._abscissa - subtrahend._abscissa, self._ordinate - subtrahend._ordinate
            )
        else:
            raise TypeError(f"Нельзя вычесть из Vector2D")

    # унарный минус (противоположный вектор)
    def __neg__(self) -> "Vector2D":
        return Vector2D(-self._abscissa, -self._ordinate)

    # преобразование в комплексное число
    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    # преобразование в вещественное число
    def __float__(self) -> float:
        return abs(self)

    # преобразование в целое число
    def __int__(self) -> int:
        return int(abs(self))

    # скалярное произведение векторов
    def __matmul__(self, other_vector: "Vector2D") -> float:
        return self._abscissa * other_vector._abscissa + self._ordinate * other_vector._ordinate

    # вычисление угла между векторами
    def get_angle(self, other_vector: "Vector2D") -> float:
        if not self or not other_vector:
            raise ValueError("Расчет угла между вектором и нулевым невозможен")

        dot_product = self @ other_vector
        norm_product = abs(self) * abs(other_vector)

        cos_angle = max(-1.0, min(1.0, dot_product / norm_product))

        return math.acos(cos_angle)

    # вычисление сопряженного вектора
    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)
