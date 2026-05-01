# ваш код
import math


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
        a, o = self.abscissa, self.ordinate
        a_str = str(int(a)) if a.is_integer() else str(a)
        o_str = str(int(o)) if o.is_integer() else str(o)
        return f"Vector2D(abscissa={a_str}, ordinate={o_str})"

    @staticmethod
    def _snap(f: float) -> float:
        return round(f, 12)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._snap(self.abscissa) == self._snap(other.abscissa) and self._snap(
            self.ordinate
        ) == self._snap(other.ordinate)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        a1, o1 = self._snap(self.abscissa), self._snap(self.ordinate)
        a2, o2 = self._snap(other.abscissa), self._snap(other.ordinate)
        return (a1 < a2) or (a1 == a2 and o1 < o2)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __abs__(self) -> float:
        return math.hypot(self.abscissa, self.ordinate)

    def __bool__(self) -> bool:
        return abs(self) > 1e-12

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa * other, self.ordinate * other)
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa / other, self.ordinate / other)
        return NotImplemented

    def __rtruediv__(self, other):
        raise TypeError(
            f"unsupported operand type(s) for /: '{type(other).__name__}' and 'Vector2D'"
        )

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        return NotImplemented

    def __rsub__(self, other):
        raise TypeError(
            f"unsupported operand type(s) for -: '{type(other).__name__}' and 'Vector2D'"
        )

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __float__(self):
        return float(abs(self))

    def __int__(self):
        return int(abs(self))

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("other must be Vector2D")
        if not self or not other:
            raise ValueError("Cannot calculate angle between zero vector")
        return math.acos((self @ other) / (abs(self) * abs(other)))

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)
