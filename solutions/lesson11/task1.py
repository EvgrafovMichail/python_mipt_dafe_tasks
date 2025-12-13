from math import acos, isclose, sqrt
from numbers import Real


class Vector2D:
    _abscissa: Real
    _ordinate: Real

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        if not isinstance(abscissa, Real):
            raise ValueError("abscissa should be real")
        if not isinstance(ordinate, Real):
            raise ValueError("ordinate should be real")

        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @abscissa.setter
    def abscissa(self, _):
        raise AttributeError()

    @property
    def ordinate(self) -> float:
        return self._ordinate

    @ordinate.setter
    def ordinate(self, _):
        raise AttributeError()

    def __str__(self):
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __repr__(self):
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __add__(self, other) -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)

        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa - other, self.ordinate - other)

        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

        return NotImplemented

    def __rsub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError

        return Vector2D(other - self.abscissa, other - self.ordinate)

    def __matmul__(self, other: "Vector2D") -> Real:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def __rmatmul__(self, other):
        return self @ other

    def __mul__(self, other: Real) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented

        return Vector2D(self.abscissa * other, self.ordinate * other)

    def __rmul__(self, other: Real) -> "Vector2D":
        return self * other

    def __truediv__(self, other: Real) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented

        return Vector2D(self.abscissa / other, self.ordinate / other)

    def __eq__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return False

        return isclose(self.abscissa, other.abscissa) and isclose(self.ordinate, other.ordinate)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented

        if isclose(self.abscissa, other.abscissa):
            return not isclose(self.ordinate, other.ordinate) and self.ordinate < other.ordinate
        return self.abscissa < other.abscissa

    def __gt__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented

        if isclose(self.abscissa, other.abscissa):
            return not isclose(self.ordinate, other.ordinate) and self.ordinate > other.ordinate
        return self.abscissa > other.abscissa

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __abs__(self):
        return sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        return not (isclose(abs(self), 0, abs_tol=10e-10))

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __float__(self):
        return abs(self)

    def __int__(self):
        return int(abs(self))

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError

        if not (bool(self) and bool(other)):
            raise ValueError("cant compute angle with zero vector")

        return acos((self @ other) / (abs(self) * abs(other)))

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)


vector1 = Vector2D(0, 10.0)
vector2 = Vector2D(0, 10.00001)
