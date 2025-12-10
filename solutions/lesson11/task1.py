from math import (
    acos,
    isclose,
    sqrt,
)
from typing import Final

EPS: Final[float] = 1e-8


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return isclose(self.abscissa, other.abscissa, abs_tol=EPS) and isclose(
            self.ordinate, other.ordinate, abs_tol=EPS
        )

    def __ne__(self, other: "Vector2D") -> bool:
        return not self == other

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        if not isclose(self.abscissa, other.abscissa, abs_tol=EPS):
            return self.abscissa > other.abscissa

        if not isclose(self.ordinate, other.ordinate, abs_tol=EPS):
            return self.ordinate > other.ordinate

        return False

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        if not isclose(self.abscissa, other.abscissa, abs_tol=EPS):
            return self.abscissa < other.abscissa

        if not isclose(self.ordinate, other.ordinate, abs_tol=EPS):
            return self.ordinate < other.ordinate

        return False

    def __ge__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        if self == other:
            return True

        return self > other

    def __le__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        if self == other:
            return True

        return self < other

    def __abs__(self) -> float:
        return sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self) -> bool:
        return abs(self) > EPS

    def __mul__(self, value: float | int) -> "Vector2D":
        if not isinstance(value, (float, int)):
            return NotImplemented

        return Vector2D(value * self.abscissa, value * self.ordinate)

    def __rmul__(self, value: float | int) -> "Vector2D":
        return self * value

    def __truediv__(self, value: float | int) -> "Vector2D":
        if not isinstance(value, (float, int)):
            return NotImplemented

        return Vector2D(self.abscissa / value, self.ordinate / value)

    def __add__(self, other: float | int) -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

        if isinstance(other, (float, int)):
            return Vector2D(self.abscissa + other, self.ordinate + other)

        return NotImplemented

    def __radd__(self, other: float | int) -> "Vector2D":
        return self + other

    def __sub__(self, other: float | int) -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

        if isinstance(other, (float, int)):
            return Vector2D(self.abscissa - other, self.ordinate - other)

        return NotImplemented

    def __rsub__(self, other) -> None:
        if not isinstance(other, (float, int)):
            return NotImplemented

        raise TypeError("Reverse subtraction (number - Vector2D) is undefined.")

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.abscissa, -self.ordinate)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError()

        if not (self and other):
            raise ValueError("Cannot compute angle with zero vector")

        return acos((self @ other) / (abs(self) * abs(other)))
