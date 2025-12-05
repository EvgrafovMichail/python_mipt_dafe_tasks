from math import acos, isclose
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __str__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        return isclose(self.abscissa, other.abscissa) and isclose(self.ordinate, other.ordinate)

    def __ne__(self, other: "Vector2D") -> bool:
        return not (self == other)

    def __gt__(self, other: "Vector2D") -> bool:
        return (
            self.abscissa > other.abscissa
            or self.abscissa == other.abscissa
            and self.ordinate > other.ordinate
        )

    def __lt__(self, other: "Vector2D") -> bool:
        return (
            self.abscissa < other.abscissa
            or self.abscissa == other.abscissa
            and self.ordinate < other.ordinate
        )

    def __ge__(self, other: "Vector2D") -> bool:
        return self > other or self == other

    def __le__(self, other: "Vector2D") -> bool:
        return self < other or self == other

    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __mul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        return Vector2D(self.abscissa * scale, self.ordinate * scale)

    def __rmul__(self, scale: Real) -> "Vector2D":
        return self * scale

    def __truediv__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        return self * (1 / scale)

    def __add__(self, other) -> "Vector2D":
        if not isinstance(other, Vector2D | Real):
            return NotImplemented

        if isinstance(other, Real):
            other = Vector2D(abscissa=other, ordinate=other)

        return Vector2D(
            abscissa=self.abscissa + other.abscissa, ordinate=self.ordinate + other.ordinate
        )

    def __radd__(self, other: Real) -> "Vector2D":
        return self + other

    def __sub__(self, other) -> "Vector2D":
        return self + (-1 * other)

    def __rsub__(self, other: "Vector2D") -> "Vector2D":
        return other + (-1 * self)

    def __neg__(self) -> "Vector2D":
        return -1 * self

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)

    def __complex__(self):
        return complex(real=self.abscissa, imag=self.ordinate)

    def __matmul__(self, other: "Vector2D") -> float:
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def __rmatmul__(self, other: "Vector2D") -> float:
        return self @ other

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if isclose(abs(self), 0) or isclose(abs(other), 0):
            raise ValueError("Расчет угла между данным вектором и нулевым вектором невозможен")

        return acos(self @ other / (abs(self) * abs(other)))
