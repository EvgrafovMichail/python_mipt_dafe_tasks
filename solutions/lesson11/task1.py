import math
from numbers import Real
from typing import Union


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
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            not math.isclose(self.abscissa, other.abscissa) and self.abscissa > other.abscissa
        ) or (
            math.isclose(self.abscissa, other.abscissa)
            and not math.isclose(self.ordinate, other.ordinate)
            and self.ordinate > other.ordinate
        )

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            not math.isclose(self.abscissa, other.abscissa) and self.abscissa < other.abscissa
        ) or (
            math.isclose(self.abscissa, other.abscissa)
            and not math.isclose(self.ordinate, other.ordinate)
            and self.ordinate < other.ordinate
        )

    def __ge__(self, other: "Vector2D") -> bool:
        return self == other or self > other

    def __le__(self, other: "Vector2D") -> bool:
        return self == other or self < other

    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not math.isclose(abs(self), 0, abs_tol=1e-18)

    def __mul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented
        return Vector2D(self.abscissa * scale, self.ordinate * scale)

    def __rmul__(self, scale: Real) -> "Vector2D":
        return self * scale

    def __truediv__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        if math.isclose(scale, 0):
            raise ZeroDivisionError("division by zero")
        return Vector2D(self.abscissa / scale, self.ordinate / scale)

    def __rtruediv__(self, other):
        return NotImplemented

    def __add__(self, other: Union["Vector2D", Real]) -> "Vector2D":
        if not isinstance(other, Vector2D | Real):
            return NotImplemented

        if isinstance(other, Real):
            other = Vector2D(abscissa=other, ordinate=other)

        return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

    def __radd__(self, other: Real) -> "Vector2D":
        return self + other

    def __sub__(self, other: Union["Vector2D", Real]) -> "Vector2D":
        if not isinstance(other, Vector2D | Real):
            return NotImplemented

        if isinstance(other, Real):
            other = Vector2D(abscissa=other, ordinate=other)

        return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

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
            raise TypeError
        if (math.isclose(self.abscissa, 0) and math.isclose(self.ordinate, 0)) or (
            math.isclose(other.abscissa, 0) and math.isclose(other.ordinate, 0)
        ):
            raise ValueError(
                "calculating the angle between this vector and the zero vector is not possible"
            )

        cos_angle = (self @ other) / (abs(self) * abs(other))
        return math.acos(cos_angle)
