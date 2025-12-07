import math
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float
    def __init__(self, abscissa = 0.0, ordinate = 0.0):
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __str__(self):
        return f'Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})'

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self._abscissa, other._abscissa) and math.isclose(self._ordinate, other._ordinate)

    def __ne__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self._abscissa < other._abscissa and not math.isclose(self._abscissa, other._abscissa)) \
            or (self._ordinate < other._ordinate and not math.isclose(self._ordinate, other._ordinate) \
            and math.isclose(self._abscissa, other._abscissa))

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self < other and not self == other

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self < other or self == other

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self > other or self == other

    def __abs__(self):
        return (self._abscissa**2 + self._ordinate**2)**0.5

    def __bool__(self):
        return not math.isclose(abs(self), 0, abs_tol=1e-15)

    def __mul__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        return Vector2D(self._abscissa * other, self._ordinate * other)

    def __rmul__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        return Vector2D(self._abscissa / other, self._ordinate / other)

    def __rtruediv__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        raise TypeError()

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        elif isinstance(other, Real):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        if not isinstance(other, Real) and not isinstance(other, Vector2D):
            return NotImplemented
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        elif isinstance(other, Real):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if not isinstance(other, Real) and not isinstance(other, Vector2D):
            return NotImplemented
        elif isinstance(other, Vector2D):
            return Vector2D(-self._abscissa + other._abscissa, -self._ordinate + other._ordinate)
        raise TypeError

    def __neg__(self):
        return Vector2D(-self._abscissa, -self._ordinate)

    def __complex__(self):
        return complex(self._abscissa, self._ordinate)

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return abs(self)

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other) -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        elif not (bool(self) and bool(other)):
            raise ValueError('Calculating an angle with a zero vector is not possible')
        return math.acos((self @ other) / (abs(self) * abs(other)))




