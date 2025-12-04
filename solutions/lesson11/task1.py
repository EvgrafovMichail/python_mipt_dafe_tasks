import math
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa=0.0, ordinate=0.0) -> None:
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
            return NotImplemented
        return math.isclose(self._abscissa, other._abscissa) and math.isclose(
            self._ordinate, other._ordinate
        )

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa < other.abscissa
        return self.ordinate < other.ordinate and not math.isclose(self.ordinate, other.ordinate)

    def __le__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self < other or self == other

    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not math.isclose(abs(self), 0, rel_tol=1e-9, abs_tol=1e-12)

    def __mul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented
        return Vector2D(self.abscissa * scale, self.ordinate * scale)

    def __rmul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented
        return Vector2D(self.abscissa * scale, self.ordinate * scale)

    def __truediv__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented
        return Vector2D(self.abscissa / scale, self.ordinate / scale)

    def __add__(self, other: "Vector2D | Real") -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return NotImplemented

    def __radd__(self, other: Real) -> "Vector2D":
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return NotImplemented

    def __sub__(self, other: "Vector2D | Real") -> "Vector2D":
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        raise TypeError()

    def __rsub__(self, other):
        raise TypeError()

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return int(abs(self))

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError()
        if not self or not other:
            raise ValueError(
                "Calculating the angle between this vector and the zero vector is not possible"
            )

        dot = self @ other
        cos = dot / (abs(self) * abs(other))
        cos = max(-1.0, min(1.0, cos))
        return math.acos(cos)

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)
