from math import acos, isclose, sqrt


class Vector2D:
    __slots__ = ("_abscissa", "_ordinate")

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return isclose(self.abscissa, other.abscissa) and isclose(self.ordinate, other.ordinate)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not isclose(self.abscissa, other.abscissa):
            return self.abscissa < other.abscissa
        if not isclose(self.ordinate, other.ordinate):
            return self.ordinate < other.ordinate
        return False

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return other < self

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return other <= self

    def __abs__(self):
        return sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        EPS = 1e-16
        return not isclose(abs(self), 0.0, rel_tol=0.0, abs_tol=EPS)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa * other, self.ordinate * other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("деление на ноль")
            return Vector2D(self.abscissa / other, self.ordinate / other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        return NotImplemented

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __float__(self):
        return abs(self)

    def __int__(self):
        return int(abs(self))

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("объект не Vector2D")

        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("Расчет угла между данным вектором и нулевым вектором невозможен")

        cos_value = (self @ other) / (abs(self) * abs(other))
        return acos(cos_value)

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)
