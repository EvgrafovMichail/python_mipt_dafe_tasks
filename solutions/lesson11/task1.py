import math
from numbers import Real
from typing import Union


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __str__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        return math.isclose(self._abscissa, other._abscissa) and math.isclose(
            self._ordinate, other._ordinate
        )

    def __lt__(self, other: "Vector2D") -> bool:
        return (
            self._abscissa < other._abscissa
            or self._abscissa == other._abscissa
            and self._ordinate < other._ordinate
        )

    def __le__(self, other: "Vector2D") -> bool:
        return self < other or self == other

    def __bool__(self) -> bool:
        return not (self._abscissa == 0 and self._ordinate == 0)

    def __mul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        abscissa = self._abscissa * scale
        ordinate = self._ordinate * scale
        return Vector2D(abscissa, ordinate)

    def __rmul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        abscissa = self._abscissa * scale
        ordinate = self._ordinate * scale
        return Vector2D(abscissa, ordinate)

    def __truediv__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        return self * (1 / scale)

    def __add__(self, other: Union["Vector2D", Real]) -> "Vector2D":
        if isinstance(other, Real):
            abscissa = self._abscissa + other
            ordinate = self._ordinate + other
            return Vector2D(abscissa, ordinate)

        if isinstance(other, Vector2D):
            abscissa = self._abscissa + other._abscissa
            ordinate = self._ordinate + other._ordinate
            return Vector2D(abscissa, ordinate)
        return NotImplemented

    def __radd__(self, other: Union["Vector2D", Real]) -> "Vector2D":
        return self + other

    def __sub__(self, other: Union["Vector2D", Real]) -> "Vector2D":
        if isinstance(other, Real):
            return self + (-other)
        if isinstance(other, Vector2D):
            abscissa = self._abscissa - other._abscissa
            ordinate = self._ordinate - other._ordinate
            return Vector2D(abscissa, ordinate)
        return NotImplemented

    def __rsub__(self, other: Union["Vector2D", Real]) -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(other, other) - self
        if isinstance(other, Vector2D):
            abscissa = other._abscissa - self._abscissa
            ordinate = other._ordinate - self._ordinate
            return Vector2D(abscissa, ordinate)
        return NotImplemented

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self._abscissa, -self._ordinate)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return math.floor(abs(self))

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def __abs__(self) -> float:
        return math.sqrt(self._abscissa**2 + self._ordinate**2)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not (bool(other) and bool(self)):
            raise ValueError
        angle = (self @ other) / (abs(self) * abs(other))
        return math.acos(angle)


vector = Vector2D(1, 3)
print(vector.abscissa, vector.ordinate)
# 1 3

vector = Vector2D()
print(vector.abscissa, vector.ordinate)
# 0 0

vector = Vector2D(1, 3)
print(vector)
# Vector2D(abscissa=1, ordinate=3)

vector = Vector2D(1, 2)
vector2 = Vector2D(1, 3)
print(vector != vector2)
print(vector < vector2)
print(abs(vector))
print(bool(vector))


vector = Vector2D(1, 1)
print(vector * 5)
# Vector2D(abscissa=5, ordinate=5)
print(5 * vector)
# Vector2D(abscissa=5, ordinate=5)
print((5 * vector) is vector)
# False

vector = Vector2D(5, 5)
print(vector / 5)
# Vector2D(abscissa=1, ordinate=1)
print((vector / 5) is vector)
# False
# print(5 / vector)
# # TypeError

vector = Vector2D(7, 7)
print(vector + 5)
# Vector2D(abscissa=1, ordinate=1)
print((vector / 5) is vector)
print(vector + vector2)
print(5 + vector2)
print("минус:")
print(vector - 5)
# Vector2D(abscissa=1, ordinate=1)

print(vector - vector2)
print(5 - vector2)

print("минус:")
print(-vector)
print(complex(vector))
print(float(vector))
print(int(vector))


vector1 = Vector2D(0, 1)
vector2 = Vector2D(1, 0)
print(vector1 @ vector2)
print(vector1.get_angle(vector2))
vector1 = Vector2D(5, 4)
print(vector1.conj())
print(vector > vector2)
print(vector2 < vector)
