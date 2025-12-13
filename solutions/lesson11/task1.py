from math import sqrt
import math


class Vector2D:
    def __init__(self, abscissa=0.0, ordinate=0.0):
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
            return False
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate < other.ordinate
        return self.abscissa < other.abscissa

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return True
            return self.ordinate <= other.ordinate
        return self.abscissa < other.abscissa

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate > other.ordinate
        return self.abscissa > other.abscissa

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return True
            return self.ordinate >= other.ordinate
        return self.abscissa > other.abscissa

    def __abs__(self):
        return sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        return not (
            math.isclose(self.abscissa, 0.0, abs_tol=1e-15)
            and math.isclose(self.ordinate, 0.0, abs_tol=1e-15)
        )

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * k, self.ordinate * k)

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        if k == 0:
            raise ZeroDivisionError()
        return Vector2D(self.abscissa / k, self.ordinate / k)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        return NotImplemented

    def __rsub__(self, other):
        return NotImplemented

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __float__(self):
        return float(abs(self))

    def __int__(self):
        return int(float(self))

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Аргумент не типа Vector2D")

        length_self = float(self)
        length_other = float(other)

        if math.isclose(length_self, 0.0) or math.isclose(length_other, 0.0):
            raise ValueError("Нельзя посчитать угол между ненулевым и нулевым вектором")

        cos_angle = (self @ other) / (length_self * length_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))

        return math.acos(cos_angle)

    def conj(self):
        return Vector2D(self.abscissa, -self.ordinate)
