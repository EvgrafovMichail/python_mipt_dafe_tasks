import math
from numbers import Real


class Vector2D:
    def __init__(self, abscissa=0.0, ordinate=0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    def __str__(self):
        abscissa_str = (
            str(int(self._abscissa)) if self._abscissa.is_integer() else str(self._abscissa)
        )
        ordinate_str = (
            str(int(self._ordinate)) if self._ordinate.is_integer() else str(self._ordinate)
        )
        return f"Vector2D(abscissa={abscissa_str}, ordinate={ordinate_str})"

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __ne__(self, other):
        if not isinstance(other, Vector2D):
            return True
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError

        if self.__eq__(other):
            return False

        if math.isclose(self.abscissa, other.abscissa):
            return self.ordinate < other.ordinate
        else:
            return self.abscissa < other.abscissa

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError

        if self.__eq__(other):
            return True

        if math.isclose(self.abscissa, other.abscissa):
            return self.ordinate <= other.ordinate
        else:
            return self.abscissa < other.abscissa

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError
        return other < self

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError
        return other <= self

    def __bool__(self):
        return not (
            math.isclose(self.ordinate, 0.0, abs_tol=1e-10)
            and math.isclose(self.abscissa, 0.0, abs_tol=1e-10)
        )

    def __abs__(self):
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    # сложение и вычитание

    def __add__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        else:
            raise TypeError

    def __radd__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        else:
            raise TypeError

    def __rsub__(self, other):
        raise TypeError

        # умножение и деление

    def __mul__(self, other):
        if not isinstance(other, Real):
            raise TypeError
        return Vector2D(self.abscissa * other, self.ordinate * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, Real):
            raise TypeError

        return Vector2D(self.abscissa / other, self.ordinate / other)

    def __rtruediv__(self, other):
        raise TypeError

    # унарный минус

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    # комплексное число и преобразование в типы

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return abs(self)

    # скалярное произведение

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError

        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def __rmatmul__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError
        return self.__matmul__(other)

    def conj(self) -> "Vector2D":
        # ваш код
        # я полагаю что эта функция нужна для
        # вычисления сопряженного вектора
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError

        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("расчет угла между данным вектором и нулевым вектором невозможен")

        # вычисляем косинус угла
        cos_theta = (self @ other) / (abs(self) * abs(other))

        # ограничиваем значение чтобы не было ошибок с округлением
        if cos_theta > 1:
            cos_theta = 1
        if cos_theta < -1:
            cos_theta = -1

        return math.acos(cos_theta)

    # ваш код
