from math import acos, hypot, isclose
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return isclose(self._ordinate, other._ordinate) and isclose(self._abscissa, other._abscissa)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self == other

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            (not isclose(self._abscissa, other._abscissa))
            and self._abscissa < other._abscissa
            or (
                isclose(self._abscissa, other._abscissa)
                and self._ordinate < other._ordinate
                and not isclose(self._ordinate, other._ordinate)
            )
        )

    def __le__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa < other._abscissa or (
            isclose(self._abscissa, other._abscissa) and self._ordinate <= other._ordinate
        )

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            (not isclose(self._abscissa, other._abscissa))
            and self._abscissa > other._abscissa
            or (
                isclose(self._abscissa, other._abscissa)
                and self._ordinate > other._ordinate
                and not isclose(self._ordinate, other._ordinate)
            )
        )

    def __ge__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa > other._abscissa or (
            isclose(self._abscissa, other._abscissa) and self._ordinate >= other._ordinate
        )

    def __bool__(self) -> bool:
        return not (isclose(self._abscissa, 0.0) and isclose(self._ordinate, 0.0))

    def __abs__(self) -> float:
        return hypot(self._abscissa, self._ordinate)

    def __mul__(self, other: Real) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented
        return Vector2D(self._abscissa * other, self._ordinate * other)

    def __rmul__(self, other) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented
        return self * other

    def __truediv__(self, other: Real) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented
        return Vector2D(self._abscissa / other, self._ordinate / other)

    def __rtruediv__(self, other: Real):
        if not isinstance(other, Real):
            return NotImplemented
        raise TypeError("Non-existent operation")

    def __add__(self, other) -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        elif isinstance(other, Real):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        return NotImplemented

    def __radd__(self, other) -> "Vector2D":
        return self + other

    def __sub__(self, other) -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        return NotImplemented

    def __rsub__(self, other) -> "Vector2D":
        if not isinstance(other, Real | Vector2D):
            return NotImplemented
        raise TypeError("Non-existent operation")

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self._abscissa, -self._ordinate)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)

    def __matmul__(self, other) -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def get_angle(self, other) -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("other is not a Vector2D")
        if not bool(self) or not bool(other):
            raise ValueError(
                f"It is not possible to calculate the angle between {self} and {other}"
            )

        cos = self @ other / (abs(self) * abs(other))
        if cos >= 1:
            return acos(1.0)
        elif cos <= -1:
            return acos(-1)
        return acos(cos)

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)
