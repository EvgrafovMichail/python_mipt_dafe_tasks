import math
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0, ordinate: float = 0) -> None:
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

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self._abscissa, other.abscissa) and math.isclose(
            self._ordinate, other.ordinate
        )

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        abscissas_equal = math.isclose(self._abscissa, other.abscissa)
        return self != other and (
            (not abscissas_equal and self._abscissa > other.abscissa)
            or (abscissas_equal and self._ordinate > other.ordinate)
        )

    def __ge__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self == other or self > other

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not (self == other or self > other)

    def __le__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self == other or self < other

    def __abs__(self) -> float:
        return (self._abscissa**2 + self._ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not math.isclose(abs(self), 0, abs_tol=1e-15)

    def __mul__(self, other: int | float) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented
        return Vector2D(self._abscissa * other, self._ordinate * other)

    def __rmul__(self, other: int | float) -> "Vector2D":
        return self * other

    def __truediv__(self, other: int | float) -> "Vector2D":
        if not isinstance(other, Real):
            return NotImplemented
        return Vector2D(self._abscissa / other, self._ordinate / other)

    def __add__(self, other: "int | float | Vector2D") -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other.abscissa, self._ordinate + other.ordinate)
        else:
            return NotImplemented

    def __radd__(self, other: int | float) -> "Vector2D":
        return self + other

    def __neg__(self) -> "Vector2D":
        return Vector2D(-1 * self._abscissa, -1 * self._ordinate)

    def __sub__(self, other: "int | float | Vector2D") -> "Vector2D":
        return self + (-other)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other.abscissa + self._ordinate * other.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError(f"Can't calculate angle between Vector2D and {type(other).__name__}")
        zero_vec = Vector2D(0, 0)
        if self == zero_vec or other == zero_vec:
            raise ValueError("Can't calculate angle between vector and zero-vector")
        return math.acos(self @ other / abs(self) / abs(other))
