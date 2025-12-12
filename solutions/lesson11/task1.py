import math


class Vector2D:
    def __init__(self, abscissa: int | float = 0.0, ordinate: int | float = 0.0) -> None:
        self._abscissa: int | float = abscissa
        self._ordinate: int | float = ordinate

    @property
    def abscissa(self) -> int | float:
        return self._abscissa

    @property
    def ordinate(self) -> int | float:
        return self._ordinate

    """isclose из math не подходит"""

    @staticmethod
    def _isclose(a: float, b: float):
        return abs(a - b) <= 1e-9

    def __str__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self._isclose(self.abscissa, other.abscissa) and self._isclose(
            self.ordinate, other.ordinate
        )

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return (
            not self._isclose(self.abscissa, other.abscissa) and self.abscissa > other.abscissa
        ) or (
            self._isclose(self.abscissa, other.abscissa)
            and not self._isclose(self.ordinate, other.ordinate)
            and self.ordinate > other.ordinate
        )

    def __ge__(self, other: "Vector2D") -> bool:
        return self > other or self == other

    def __abs__(self) -> float:
        return math.sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self) -> bool:
        return not self._isclose(0, abs(self))

    def __mul__(self, scalar: int | float) -> "Vector2D":
        if not isinstance(scalar, int | float):
            return NotImplemented

        return Vector2D(self.abscissa * scalar, self.ordinate * scalar)

    def __rmul__(self, scalar: int | float) -> "Vector2D":
        return self * scalar

    def __truediv__(self, scalar: int | float) -> "Vector2D":
        if not isinstance(scalar, int | float):
            return NotImplemented

        return Vector2D(self.abscissa / scalar, self.ordinate / scalar)

    def __add__(self, other: int | float) -> "Vector2D":
        if not isinstance(other, int | float | Vector2D):
            return NotImplemented

        if isinstance(other, int | float):
            other = Vector2D(other, other)

        return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

    def __radd__(self, other: int | float) -> "Vector2D":
        return self + other

    def __neg__(self) -> "Vector2D":
        return self * -1

    def __sub__(self, other: int | float) -> "Vector2D":
        if isinstance(other, int | float | Vector2D):
            other = -other

        return self + other

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return int(abs(self))

    def __matmul__(self, other: "Vector2D") -> int | float:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError

        if other == Vector2D(0, 0) or self == Vector2D(0, 0):
            raise ValueError("Нельзя рассчитать угол между нулевым и любым другим вектором.")

        return math.acos((self @ other) / (abs(self) * abs(other)))

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)
