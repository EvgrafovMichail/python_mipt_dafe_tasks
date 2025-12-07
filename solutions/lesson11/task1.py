from math import isclose, sqrt, acos


class Vector2D:
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return isclose(self._abscissa, other._abscissa) and isclose(self._ordinate, other._ordinate)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError

        if self == other:
            return False
        if not isclose(self._abscissa, other._abscissa):
            return self._abscissa < other._abscissa
        return self._ordinate < other._ordinate

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        return other < self

    def __le__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        return self < other or self == other

    def __ge__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        return other <= self

    def __abs__(self) -> float:
        return sqrt(self._abscissa**2 + self._ordinate**2)

    def __bool__(self) -> bool:
        return not isclose(abs(self), 0, abs_tol=1e-9)

    def __mul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return Vector2D(self._abscissa * other, self._ordinate * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        if isclose(other, 0.0):
            raise ValueError
        _inverse = 1.0 / other
        return Vector2D(self._abscissa * _inverse, self._ordinate * _inverse)

    def __rtruediv__(self, other):
        raise TypeError

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        elif isinstance(other, int | float):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        elif isinstance(other, int | float):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        raise TypeError

    def __rsub__(self, other):
        raise TypeError

    def __neg__(self):
        return Vector2D(-self._abscissa, -self._ordinate)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return int(abs(self))

    def __matmul__(self, other) -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def get_angle(self, other) -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        if not bool(self) or not bool(other):
            raise ValueError(
                "Calculating the angle between the vector and the zero vector is not possible"
            )
        product = self @ other
        abs_product = abs(self) * abs(other)

        cos_angle = max(-1.0, min(1.0, product / abs_product))
        return acos(cos_angle)

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)
