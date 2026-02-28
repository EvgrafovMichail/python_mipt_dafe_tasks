import math
from numbers import Real


class Vector2D:
    def __init__(self, abscissa=0.0, ordinate=0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self._abscissa, other._abscissa) and math.isclose(
            self._ordinate, other._ordinate
        )

    def __ne__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self.__eq__(other)

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        if self.__eq__(other):
            return False

        if not math.isclose(self._abscissa, other._abscissa):
            return self._abscissa > other._abscissa

        return self._ordinate > other._ordinate

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        if self.__eq__(other):
            return False

        if not math.isclose(self._abscissa, other._abscissa):
            return self._abscissa < other._abscissa

        return self._ordinate < other._ordinate

    def __ge__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.__eq__(other) or self.__lt__(other)

    def __abs__(self) -> float:
        return math.sqrt(self._abscissa**2 + self._ordinate**2)

    def __bool__(self) -> bool:
        return not (
            math.isclose(self._abscissa, 0, abs_tol=1e-14)
            and math.isclose(self._ordinate, 0, abs_tol=1e-14)
        )

    def __mul__(self, numb: Real) -> "Vector2D":
        if not isinstance(numb, Real):
            return NotImplemented

        return Vector2D(self._abscissa * numb, self._ordinate * numb)

    def __rmul__(self, numb: Real) -> "Vector2D":
        return self.__mul__(numb)

    def __truediv__(self, numb: Real) -> "Vector2D":
        if not isinstance(numb, Real):
            return NotImplemented

        return Vector2D(self._abscissa * (1 / numb), self._ordinate * (1 / numb))

    def __add__(self, other: "Vector2D | Real") -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        else:
            return NotImplemented

    def __radd__(self, other: "Vector2D | Real") -> "Vector2D":
        return self.__add__(other)

    def __sub__(self, other: "Vector2D | Real") -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        else:
            return NotImplemented

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self._abscissa, -self._ordinate)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return float(abs(self))

    def __complex__(self):
        return complex(real=self._abscissa, imag=self._ordinate)

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        scalar = self._abscissa * other._abscissa + self._ordinate * other._ordinate
        return scalar

    def __rmatmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self @ other

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError

        if (self._abscissa == 0 and self._ordinate == 0) or (
            other._abscissa == 0 and other._ordinate == 0
        ):
            raise ValueError("Расчет угла между данным вектором и нулевым вектором невозможен")

        cos_angle = (self @ other) / (abs(self) * abs(other))
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle = math.acos(cos_angle)
        return angle
