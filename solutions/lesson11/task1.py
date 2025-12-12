import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2D:
    abscissa: float = 0
    ordinate: float = 0

    eps = 1e-10

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (abs(self.abscissa - other.abscissa) < self.eps and
                abs(self.ordinate - other.ordinate) < self.eps)

    def __ne__(self, other):
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        return not eq_result

    def __lt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented

        if abs(self.abscissa - other.abscissa) >= self.eps:
            return self.abscissa < other.abscissa
        else:
            if abs(self.ordinate - other.ordinate) < self.eps:
                return False
            return self.ordinate < other.ordinate

    def __le__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented

        if abs(self.abscissa - other.abscissa) >= self.eps:
            return self.abscissa < other.abscissa
        else:
            if abs(self.ordinate - other.ordinate) < self.eps:
                return True
            return self.ordinate <= other.ordinate

    def __gt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return other < self

    def __ge__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return other <= self

    def __bool__(self):
        return abs(self.abscissa) > self.eps or abs(self.ordinate) > self.eps

    def __mul__(self, other: float):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * other, self.ordinate * other)

    def __rmul__(self, other: float):
        return self.__mul__(other)

    def __truediv__(self, num: float):
        if not isinstance(num, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa / num, self.ordinate / num)

    def __rtruediv__(self, num: float):
        raise TypeError

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        return NotImplemented

    def __matmul__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def __abs__(self):
        return math.hypot(self.abscissa, self.ordinate)

    def get_angle(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            raise TypeError
        if abs(self) != 0 and abs(other) != 0:
            cos = (self @ other) / (abs(self) * abs(other))
            return math.acos(cos)
        raise ValueError

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __float__(self):
        return float(abs(self))

    def __int__(self):
        return int(float(self))

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)
