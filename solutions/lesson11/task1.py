import math
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self._abscissa, other._abscissa, abs_tol=1e-14) and math.isclose(
            self._ordinate, other._ordinate, abs_tol=1e-14
        )

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError

        if self == other:
            return False

        if math.isclose(self._abscissa, other._abscissa, abs_tol=1e-14):
            return self._ordinate < other._ordinate
        return self._abscissa < other._abscissa

    def __le__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError

        if self == other:
            return True

        if math.isclose(self._abscissa, other._abscissa, abs_tol=1e-14):
            return self._ordinate <= other._ordinate
        return self._abscissa <= other._abscissa

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError

        if self == other:
            return False

        if math.isclose(self._abscissa, other._abscissa, abs_tol=1e-14):
            return self._ordinate > other._ordinate
        return self._abscissa > other._abscissa

    def __ge__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError

        if self == other:
            return True

        if math.isclose(self._abscissa, other._abscissa, abs_tol=1e-14):
            return self._ordinate >= other._ordinate
        return self._abscissa >= other._abscissa

    def __abs__(self) -> float:
        return (self._abscissa**2 + self._ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not math.isclose(self.__abs__(), 0, abs_tol=1e-14)

    def __mul__(self, number: Real) -> "Vector2D":
        if not isinstance(number, Real):
            return NotImplemented
        new_vector = Vector2D(self._abscissa * number, self._ordinate * number)
        return new_vector

    def __rmul__(self, number: Real) -> "Vector2D":
        return self * number

    def __truediv__(self, number: Real) -> "Vector2D":
        return self * number ** (-1)

    def __add__(self, other) -> "Vector2D":
        if not isinstance(other, Vector2D | Real):
            return NotImplemented

        if isinstance(other, Real):
            new_vector = Vector2D(self._abscissa + other, self._ordinate + other)

        if isinstance(other, Vector2D):
            new_vector = Vector2D(
                self._abscissa + other._abscissa, self._ordinate + other._ordinate
            )

        return new_vector

    def __radd__(self, other) -> "Vector2D":
        return self + other

    def __sub__(self, other) -> "Vector2D":
        return self + other * (-1)

    def __neg__(self) -> "Vector2D":
        return self * (-1)

    def __complex__(self):
        return complex(self._abscissa, self._ordinate)

    def __float__(self):
        return self.__abs__()

    def __int__(self):
        return int(self.__float__())

    def __matmul__(self, other) -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def conj(self) -> "Vector2D":
        # Специально для Вас, Евгений, информативные имена
        conjugate_vector2D = Vector2D(self._abscissa, -self._ordinate)
        return conjugate_vector2D

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        if self == Vector2D(0, 0) or other == Vector2D(0, 0):
            raise ValueError("Calculation of the angle between the zero vector is impossible")
        return math.acos((self @ other) / (self.__abs__() * other.__abs__()))
