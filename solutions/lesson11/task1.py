from math import acos, isclose, sqrt


class Vector2D:
    __slots__ = ("__abscissa", "__ordinate")

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self.__abscissa = float(abscissa)
        self.__ordinate = float(ordinate)

    @property
    def abscissa(self):
        return self.__abscissa

    @property
    def ordinate(self):
        return self.__ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return isclose(self.abscissa, other.abscissa) and isclose(self.ordinate, other.ordinate)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if isclose(self.abscissa, other.abscissa):
            if isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate < other.ordinate
        return self.abscissa < other.abscissa

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __abs__(self):
        return sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self):
        tol = 1e-12
        return not (
            isclose(self.abscissa, 0.0, abs_tol=tol) and isclose(self.ordinate, 0.0, abs_tol=tol)
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
        if isclose(scalar, 0.0):
            raise ZeroDivisionError("division by zero")
        return Vector2D(self.abscissa / scalar, self.ordinate / scalar)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        return NotImplemented

    def __rsub__(self, other):
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
            raise TypeError("other must be Vector2D")

        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("Невозможно вычислить угол между данным вектором и нулевым вектором")

        scalar_product = self @ other
        product_of_lengths = abs(self) * abs(other)

        cos_value = max(-1.0, min(1.0, scalar_product / product_of_lengths))
        return acos(cos_value)

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)
