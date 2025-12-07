from dataclasses import dataclass, field
import math


@dataclass(frozen=True)
class Vector2D:
    abscissa: float = field(default=0.0)
    ordinate: float = field(default=0.0)

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other) -> bool:
        try:
            return math.isclose(self.abscissa, other.abscissa) and math.isclose(
                self.ordinate, other.ordinate
            )
        except AttributeError:
            return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self.abscissa < other.abscissa or (
            math.isclose(self.abscissa, other.abscissa) and self.ordinate < other.ordinate
        )

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self == other or self < other

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented

        return not self <= other

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self == other or self > other

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def __abs__(self):
        return math.sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        return self.__abs__() != 0.0

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __float__(self):
        return self.__abs__()

    def __int__(self):
        return int(self.__abs__())

    def __neg__(self):
        return self * (-1)

    def conjugate(self):
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError(
                f"Операция 'get_angle' не поддерживается между 'Vector2D' и '{type(other).__name__}'"
            )

        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("расчет угла между данным вектором и нулевым вектором невозможен")

        dot_product = self @ other
        magnitudes_product = abs(self) * abs(other)

        cosine_angle = dot_product / magnitudes_product
        cosine_angle = max(-1.0, min(1.0, cosine_angle))

        return math.acos(cosine_angle)

    def __add__(self, other):
        try:
            new_abscissa = self.abscissa + other.abscissa
            new_ordinate = self.ordinate + other.ordinate
            return Vector2D(new_abscissa, new_ordinate)
        except AttributeError:
            return Vector2D(self.abscissa + other, self.ordinate + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            new_abscissa = self.abscissa - other.abscissa
            new_ordinate = self.ordinate - other.ordinate
            return Vector2D(new_abscissa, new_ordinate)
        except AttributeError:
            return Vector2D(self.abscissa - other, self.ordinate - other)

    def __rsub__(self, other):
        return Vector2D(other - self.abscissa, other - self.ordinate)

    def __mul__(self, scalar):
        return Vector2D(self.abscissa * scalar, self.ordinate * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("division by zero")

        return self * (1.0 / scalar)
