from math import acos, isclose
from numbers import Real


class Vector2D:
    _abscissa: float = 0
    _ordinate: float = 0

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa: float = abscissa
        self._ordinate: float = ordinate

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return isclose(self._abscissa, other._abscissa) and isclose(self._ordinate, other._ordinate)

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if isclose(self._abscissa, other._abscissa):
            return (
                not isclose(self._ordinate, other._ordinate)
            ) and self._ordinate > other._ordinate
        elif self._abscissa > other._abscissa:
            return True
        else:
            return False

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if isclose(self._abscissa, other._abscissa):
            return (
                not isclose(self._ordinate, other._ordinate)
            ) and self._ordinate < other._ordinate
        elif self._abscissa < other._abscissa:
            return True
        else:
            return False

    def __ge__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        equal = self == other
        absc = self._abscissa > other._abscissa
        ordn = isclose(self._abscissa, other._abscissa) and self._ordinate > other._ordinate
        return equal or (absc or ordn)

    def __le__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        equal = self == other
        absc = self._abscissa < other._abscissa
        ordn = isclose(self._abscissa, other._abscissa) and self._ordinate < other._ordinate
        return equal or (absc or ordn)

    def __abs__(self) -> float:
        len = (self._abscissa**2 + self._ordinate**2) ** 0.5
        return len

    def __bool__(self) -> bool:
        return not isclose(abs(self), 0, abs_tol=10e-9)

    def __mul__(self, num: Real) -> "Vector2D":
        if not isinstance(num, Real):
            return NotImplemented
        return Vector2D(self._abscissa * num, self._ordinate * num)

    def __rmul__(self, num: Real) -> "Vector2D":
        return self * num

    def __truediv__(self, num: Real) -> "Vector2D":
        if not isinstance(num, Real):
            return NotImplemented
        if num == 0:
            raise ZeroDivisionError()
        return Vector2D(self._abscissa / num, self._ordinate / num)

    def __add__(self, other: Real | "Vector2D") -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        return NotImplemented

    def __radd__(self, num: Real) -> "Vector2D":
        return self + num

    def __sub__(self, other: Real | "Vector2D") -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        return NotImplemented

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self._abscissa, -self._ordinate)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> Real:
        return abs(self)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __matmul__(self, other: "Vector2D") -> Real:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> Real:
        if not isinstance(other, Vector2D):
            raise TypeError
        if abs(other) == 0 or abs(self) == 0:
            raise ValueError("impossible to calculate angle between vector and zero-vector")
        return acos((self @ other) / (abs(self) * abs(other)))
