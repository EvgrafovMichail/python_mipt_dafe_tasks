import math
from typing import Any, Union


class Vector2D:
    __slots__ = ("_abscissa", "_ordinate")

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __repr__(self) -> str:
        def fmt(v: float) -> str:
            return str(int(v)) if v.is_integer() else str(v)

        return f"Vector2D(abscissa={fmt(self._abscissa)}, ordinate={fmt(self._ordinate)})"

    def __eq__(self, other: Any):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self._abscissa, other._abscissa) and math.isclose(
            self._ordinate, other._ordinate
        )

    def __lt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented

        if self.__eq__(other):
            return False

        if not math.isclose(self._abscissa, other._abscissa):
            return self._abscissa < other._abscissa

        return self._ordinate < other._ordinate

    def __le__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return other.__lt__(self)

    def __ge__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return other.__le__(self)

    def __abs__(self) -> float:
        return math.sqrt(self._abscissa**2 + self._ordinate**2)

    def __bool__(self) -> bool:
        eps = 1e-15
        return abs(self._abscissa) > eps or abs(self._ordinate) > eps

    def __add__(self, other: Union["Vector2D", float]) -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        return NotImplemented

    def __radd__(self, other: Union["Vector2D", float]) -> "Vector2D":
        return self.__add__(other)

    def __sub__(self, other: Union["Vector2D", float]) -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        return NotImplemented

    def __rsub__(self, other: Union["Vector2D", float]) -> "Vector2D":
        return NotImplemented

    def __mul__(self, scalar: float) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._abscissa * scalar, self._ordinate * scalar)

    def __rmul__(self, scalar: float) -> "Vector2D":
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if math.isclose(scalar, 0.0):
            raise ZeroDivisionError
        return Vector2D(self._abscissa / scalar, self._ordinate / scalar)

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self._abscissa, -self._ordinate)

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def __rmatmul__(self, other: "Vector2D") -> float:
        return self.__matmul__(other)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __float__(self) -> float:
        return float(abs(self))

    def __int__(self) -> int:
        return int(float(self))

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError

        if not bool(self) or not bool(other):
            raise ValueError("Расчет угла с нулевым вектором невозможен")

        dot_product = self @ other
        len_self = abs(self)
        len_other = abs(other)

        cos_angle = dot_product / (len_self * len_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))

        angle_rad = math.acos(cos_angle)
        return angle_rad
