import math
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

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __lt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            (self.abscissa < other.abscissa and not math.isclose(self.abscissa, other.abscissa))
            or (math.isclose(self.abscissa, other.abscissa) and self.ordinate < other.ordinate)
            and not math.isclose(self.ordinate, other.ordinate)
        )

    def __gt__(self, other: "Vector2D"):
        return not self < other and not self == other

    def __le__(self, other: "Vector2D"):
        return self < other or self == other

    def __ge__(self, other: "Vector2D"):
        return self > other or self == other

    def __abs__(self):
        return math.sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        return not math.isclose(abs(self), 0, abs_tol=1e-12)

    def __mul__(self, number: Real):
        if not isinstance(number, Real):
            return NotImplemented
        return Vector2D(self.abscissa * number, self.ordinate * number)

    def __rmul__(self, number: Real):
        return self * number

    def __truediv__(self, number: Real):
        if not isinstance(number, Real):
            return NotImplemented
        if math.isclose(number, 0):
            raise ZeroDivisionError
        return Vector2D(self.abscissa / number, self.ordinate / number)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return NotImplemented

    def __radd__(self, other: Real):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __float__(self):
        return abs(self)

    def __int__(self):
        return int(abs(self))

    def __matmul__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        if not self or not other:
            raise ValueError(
                "it is impossible to calculate the angle between the data vector and the \
                zero vector"
            )

        cos = (self @ other) / (abs(self) * abs(other))
        return math.acos(cos)
