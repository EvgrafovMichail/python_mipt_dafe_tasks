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
        if self.abscissa.is_integer():
            x = int(self.abscissa)
        else:
            self.abscissa

        if self.ordinate.is_integer():
            y = int(self.ordinate)
        else:
            self.ordinate

        return "Vector2D(abscissa=" + str(x) + ", ordinate=" + str(y) + ")"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __ne__(self, other):
        r = self.__eq__(other)
        if r is NotImplemented:
            return NotImplemented
        return not r

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa < other.abscissa
        if not math.isclose(self.ordinate, other.ordinate):
            return self.ordinate < other.ordinate
        return False

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa < other.abscissa
        if not math.isclose(self.ordinate, other.ordinate):
            return self.ordinate < other.ordinate
        return True

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa > other.abscissa
        if not math.isclose(self.ordinate, other.ordinate):
            return self.ordinate > other.ordinate
        return False

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa > other.abscissa
        if not math.isclose(self.ordinate, other.ordinate):
            return self.ordinate > other.ordinate
        return True

    def __abs__(self):
        return math.sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        return not (
            math.isclose(self.abscissa, 0.0, abs_tol=1e-15)
            and math.isclose(self.ordinate, 0.0, abs_tol=1e-15)
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * scalar, self.ordinate * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if math.isclose(scalar, 0.0):
            raise ZeroDivisionError("Division by zero")
        return Vector2D(self.abscissa / scalar, self.ordinate / scalar)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        else:
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
        return int(abs(self))

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Argument must be Vector2D")
        if not self or not other:
            raise ValueError("Cannot compute angle with zero vector")
        dot = self @ other
        l1 = abs(self)
        l2 = abs(other)
        cos_a = dot / (l1 * l2)
        if cos_a > 1.0:
            cos_a = 1.0
        if cos_a < -1.0:
            cos_a = -1.0
        return math.acos(cos_a)

    def conjugate(self):
        return Vector2D(self.abscissa, -self.ordinate)

    def conj(self):
        return self.conjugate()
