import math
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

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __ne__(self, other: "Vector2D") -> bool:
        return not (self == other)

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            not math.isclose(self.abscissa, other.abscissa) and self.abscissa > other.abscissa
        ) or (
            math.isclose(self.abscissa, other.abscissa)
            and self.ordinate > other.ordinate
            and not math.isclose(self.ordinate, other.abscissa)
        )

    def __lt__(self, other: "Vector2D") -> bool:
        return not (self > other or self == other)

    def __ge__(self, other) -> bool:
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not abs(self) < 1e-09

    def __mul__(self, number) -> "Vector2D":
        if not isinstance(number, Real):
            return NotImplemented
        return Vector2D(self.abscissa * number, self.ordinate * number)

    def __rmul__(self, number) -> "Vector2D":
        return self * number

    def __truediv__(self, number) -> "Vector2D":
        if not isinstance(number, Real):
            return NotImplemented
        return Vector2D(self.abscissa / number, self.ordinate / number)

    def __add__(self, other) -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        return NotImplemented

    def __radd__(self, other) -> "Vector2D":
        return self + other

    def __sub__(self, other) -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        return NotImplemented

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return int(abs(self))

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("Аргумент не является объектом Vector2D")
        if other == Vector2D(0, 0) or self == Vector2D(0, 0):
            raise ValueError("Расчет угла между вектором и нулевым вектором невозможен")
        cos_angle = (self @ other) / (abs(self) * abs(other))
        cos_angle = max(cos_angle, -1.0)
        cos_angle = min(cos_angle, 1.0)
        return math.acos(cos_angle)
