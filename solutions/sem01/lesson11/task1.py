from math import acos


class Vector2D:
    _abscissa = 0.0
    _ordinate = 0.0

    def __init__(self, abscissa=0.0, ordinate=0.0):
        self._abscissa = round(abscissa, 12)
        self._ordinate = round(ordinate, 12)

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False

        return self._ordinate == other.ordinate and self._abscissa == other.abscissa

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError()

        return self._abscissa > other.abscissa or (
            self._abscissa == other.abscissa and self._ordinate > other.ordinate
        )

    def __lt__(self, other):
        return not (self > other) and not (self == other)

    def __ge__(self, other):
        return not (self < other)

    def __le__(self, other):
        return not (self > other)

    def __abs__(self):
        return (self._abscissa**2 + self._ordinate**2) ** 0.5

    def __bool__(self):
        return abs(self) != 0

    def __mul__(self, num):
        return Vector2D(self._abscissa * num, self._ordinate * num)

    def __rmul__(self, num):
        return self * num

    def __truediv__(self, num):
        return self * (1 / num)

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other.abscissa, self._ordinate + other.ordinate)

        raise TypeError()

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Vector2D(-self._abscissa, -self._ordinate)

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return abs(self)

    def __complex__(self):
        return complex(self._abscissa, self._ordinate)

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError()

        return self._abscissa * other.abscissa + self._ordinate * other.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError()

        if (not self._abscissa and not self._ordinate) or (
            not other.abscissa and not other.ordinate
        ):
            raise ValueError("Нельзя рассчитать угол с нулевым вектором")
        return acos((self @ other) / (abs(self) * abs(other)))
