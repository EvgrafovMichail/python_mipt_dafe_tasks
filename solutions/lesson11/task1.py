import math


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa=0, ordinate=0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __float__(self: "Vector2D") -> float:
        return abs(self)

    def __int__(self: "Vector2D") -> int:
        return int(float(self))

    def __complex__(self: "Vector2D"):
        return complex(self.abscissa, self.ordinate)

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        if abs(self) > 0 and abs(other) > 0:
            return math.acos(self @ other / (abs(self) * abs(other)))
        else:
            raise ValueError("угол с вектором 0 0 не вычислить")

    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa) and math.isclose(
            self.ordinate, other.ordinate
        ):
            return True
        else:
            return False

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if self.abscissa > other.abscissa and not math.isclose(self.abscissa, other.abscissa):
            return True
        elif math.isclose(self.abscissa, other.abscissa):
            if self.ordinate > other.ordinate and not math.isclose(self.ordinate, other.ordinate):
                return True
        return False

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if self.abscissa < other.abscissa and not math.isclose(self.abscissa, other.abscissa):
            return True
        elif math.isclose(self.abscissa, other.abscissa):
            if self.ordinate < other.ordinate and not math.isclose(self.ordinate, other.ordinate):
                return True
        return False

    def __ge__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if self.abscissa > other.abscissa:
            return True
        elif math.isclose(self.abscissa, other.abscissa) and (
            math.isclose(self.ordinate, other.ordinate) or self.ordinate > other.ordinate
        ):
            return True
        else:
            return False

    def __le__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if self.abscissa < other.abscissa:
            return True
        elif math.isclose(self.abscissa, other.abscissa) and (
            math.isclose(self.ordinate, other.ordinate) or self.ordinate < other.ordinate
        ):
            return True
        else:
            return False

    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self) -> bool:
        return not math.isclose(abs(self), 0, abs_tol=1e-15)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)

        elif isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)

        else:
            return NotImplemented

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector2D(self.abscissa * other, self.ordinate * other)

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (float, int)) and other != 0:
            return Vector2D(self.abscissa / other, self.ordinate / other)

        else:
            return NotImplemented

    def __matmul__(self: "Vector2D", other: "Vector2D") -> float:
        if isinstance(self, Vector2D) and isinstance(other, Vector2D):
            return self.abscissa * other.abscissa + self.ordinate * other.ordinate
        else:
            return NotImplemented


v1 = Vector2D(1, 3)
v2 = Vector2D(1, 2)

print(v1 >= v2)


# ваш код
