import math
from numbers import Real


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self):
        return self._abscissa

    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not math.isclose(abs(self), 0, abs_tol=1e-12)

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        )

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self != other and (
            (not math.isclose(self.abscissa, other.abscissa) and self.abscissa > other.abscissa)
            or (
                math.isclose(self.abscissa, other.abscissa)
                and self.ordinate > other.ordinate
                and not math.isclose(self.ordinate, other.ordinate)
            )
        )

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self != other and (
            (not math.isclose(self.abscissa, other.abscissa) and self.abscissa < other.abscissa)
            or (
                math.isclose(self.abscissa, other.abscissa)
                and self.ordinate < other.ordinate
                and not math.isclose(self.ordinate, other.ordinate)
            )
        )

    def __ge__(self, other: "Vector2D") -> bool:
        return self == other or self > other

    def __le__(self, other: "Vector2D") -> bool:
        return self == other or self < other

    def __mul__(self, num: Real) -> "Vector2D":
        if not isinstance(num, Real):
            return NotImplemented
        return Vector2D(self.abscissa * num, self.ordinate * num)

    def __rmul__(self, num: Real) -> "Vector2D":
        return self * num

    def __truediv__(self, num: Real) -> "Vector2D":
        if not isinstance(num, Real):
            return NotImplemented
        if math.isclose(num, 0):
            raise ZeroDivisionError("division by zero")
        return Vector2D(self.abscissa / num, self.ordinate / num)

    def __rtruediv__(self, other):
        return NotImplemented

    def __add__(self, other: "Vector2D" | Real) -> "Vector2D":
        if isinstance(other, Real):
            other = Vector2D(other, other)
        elif isinstance(other, Vector2D):
            pass
        else:
            return NotImplemented

        return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

    def __radd__(self, other: Real) -> "Vector2D":
        return self + other

    def __sub__(self, other: Real | "Vector2D") -> "Vector2D":
        if isinstance(other, Real):
            other = Vector2D(other, other)
        elif isinstance(other, Vector2D):
            pass
        else:
            return NotImplemented

        return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        if (math.isclose(self.abscissa, 0) and math.isclose(self.ordinate, 0)) or (
            math.isclose(other.abscissa, 0) and math.isclose(other.ordinate, 0)
        ):
            raise ValueError(
                "calculating the angle between a given vector and the zero vector is not possible"
            )

        angle_cos = (self @ other) / (abs(self) * abs(other))
        return math.acos(angle_cos)
