from functools import total_ordering
from math import acos
from numbers import Real


@total_ordering
class Vector2D:
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self):
        x = int(self._abscissa) if self._abscissa.is_integer() else self._abscissa
        y = int(self._ordinate) if self._ordinate.is_integer() else self._ordinate
        return f"Vector2D(abscissa={x}, ordinate={y})"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        eps = 1e-10
        return (
            abs(self._abscissa - other._abscissa) < eps
            and abs(self._ordinate - other._ordinate) < eps
        )

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        eps = 1e-10
        if abs(self._abscissa - other._abscissa) > eps:
            return self._abscissa < other._abscissa
        if abs(self._ordinate - other._ordinate) > eps:
            return self._ordinate < other._ordinate
        return False

    def __abs__(self):
        return (self._abscissa**2 + self._ordinate**2) ** 0.5

    def __bool__(self):
        eps = 1e-10
        return not (abs(self._abscissa) < eps and abs(self._ordinate) < eps)

    def __mul__(self, scalar):
        if not isinstance(scalar, Real):
            return NotImplemented
        return Vector2D(self._abscissa * scalar, self._ordinate * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        if not isinstance(scalar, Real):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError
        return Vector2D(self._abscissa / scalar, self._ordinate / scalar)

    def __rtruediv__(self, scalar):
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(
                self._abscissa + other._abscissa, self._ordinate + other._ordinate
            )
        if isinstance(other, Real):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(
                self._abscissa - other._abscissa, self._ordinate - other._ordinate
            )
        if isinstance(other, Real):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        return NotImplemented

    def __rsub__(self, other):

        raise TypeError

    def __neg__(self):
        return Vector2D(-self._abscissa, -self._ordinate)

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("Нельзя нулевой вектор сюда, умник!")
        cos_angle = (self @ other) / (abs(self) * abs(other))
        cos_angle = max(-1.0, min(1.0, cos_angle))
        return acos(cos_angle)

    def __complex__(self):
        return complex(self._abscissa, self._ordinate)

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return float(abs(self))
