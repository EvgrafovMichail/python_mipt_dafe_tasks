import math
from numbers import Real


class Vector2D:
    def __init__(self, abs=0.0, ord=0.0):
        self.__abscissa = float(abs)
        self.__ordinate = float(ord)

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("Only Vector2D")

        if not self or not other:
            raise ValueError("Angle between null Vector2D.")

        return math.acos((self @ other) / (abs(self) * abs(other)))

    ###################################################

    @property
    def abscissa(self) -> float:
        return self.__abscissa

    @property
    def ordinate(self) -> float:
        return self.__ordinate

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, vec2: "Vector2D") -> bool:
        if not isinstance(vec2, Vector2D):
            return NotImplemented

        return math.isclose(self.abscissa, vec2.abscissa) and math.isclose(
            self.ordinate, vec2.ordinate
        )

    def __gt__(self, vec2: "Vector2D") -> bool:
        return self != vec2 and (
            self.abscissa > vec2.abscissa
            or (math.isclose(self.abscissa, vec2.abscissa) and self.ordinate > vec2.ordinate)
        )

    def __lt__(self, vec2: "Vector2D") -> bool:
        return self != vec2 and (
            self.abscissa < vec2.abscissa
            or (math.isclose(self.abscissa, vec2.abscissa) and self.ordinate < vec2.ordinate)
        )

    def __ge__(self, vec2: "Vector2D") -> bool:
        return self == vec2 or self > vec2

    def __le__(self, vec2: "Vector2D") -> bool:
        return self == vec2 or self < vec2

    def __abs__(self) -> float:
        return math.sqrt(self.abscissa**2 + self.ordinate**2)

    def __bool__(self) -> bool:
        return not math.isclose(abs(self), 0)

    def __mul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        return Vector2D(self.abscissa * scale, self.ordinate * scale)

    def __rmul__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        return self * scale

    def __truediv__(self, scale: Real) -> "Vector2D":
        if not isinstance(scale, Real):
            return NotImplemented

        if math.isclose(scale, 0):
            raise ZeroDivisionError

        return Vector2D(self.abscissa / scale, self.ordinate / scale)

    def __add__(self, other: "Vector2D" | Real) -> "Vector2D":
        if not isinstance(other, Vector2D | Real):
            return NotImplemented

        if isinstance(other, Real):
            other = Vector2D(other, other)

        return Vector2D(other.abscissa + self.abscissa, other.ordinate + self.ordinate)

    def __radd__(self, other: Real) -> "Vector2D":
        return self + other

    def __sub__(self, other: "Vector2D" | Real) -> "Vector2D":
        if not isinstance(other, Vector2D | Real):
            return NotImplemented

        if isinstance(other, Real):
            other = Vector2D(other, other)

        return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.abscissa, -self.ordinate)

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)

    def __matmul__(self, vec2: "Vector2D") -> float:
        if not isinstance(vec2, Vector2D):
            return NotImplemented

        return self.abscissa * vec2.abscissa + self.ordinate * vec2.ordinate
