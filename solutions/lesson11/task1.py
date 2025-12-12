from dataclasses import dataclass
from math import acos, isclose


@dataclass(eq=False, frozen=True)
class Vector2D:
    abscissa: float = 0.0
    ordinate: float = 0.0

    # def __init__(self, abscissa: float, ordinate: float):
    #     self.abscissa = abscissa
    #     self.ordinate = ordinate
    # def __repr__(self):
    #     return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"
    def __post_init__(self):
        object.__setattr__(self, "abscissa", float(self.abscissa))
        object.__setattr__(self, "ordinate", float(self.ordinate))

    @property
    def get_x(self):
        return self.abscissa

    @property
    def get_y(self):
        return self.ordinate

    def __ne__(self, other: "Vector2D"):
        return not (self == other)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return isclose(self.abscissa, other.abscissa, rel_tol=1e-9, abs_tol=1e-10) and isclose(
            self.ordinate, other.ordinate, rel_tol=1e-9, abs_tol=1e-10
        )

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (
            self.abscissa < other.abscissa
            and not (isclose(self.abscissa, other.abscissa, rel_tol=1e-9, abs_tol=1e-10))
        ) or (
            isclose(self.abscissa, other.abscissa, rel_tol=1e-9, abs_tol=1e-10)
            and self.ordinate < other.ordinate
            and not (isclose(self.ordinate, other.ordinate))
        )

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __abs__(self):
        return (self.abscissa**2 + self.ordinate**2) ** 0.5

    def __bool__(self):
        return not (isclose(abs(self), 0, abs_tol=1e-12))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa * other, self.ordinate * other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa / other, self.ordinate / other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        return NotImplemented

    def __neg__(self):
        return self * -1

    def __float__(self):
        return abs(self)

    def __int__(self):
        return int(abs(self))

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __matmul__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("other must be Vector2D")
        if isclose(abs(other), 0) or isclose(abs(self), 0):
            raise ValueError("You cannot get angle in between given vector and a zero vector")
        return acos((self @ other) / (abs(self) * abs(other)))

    def conj(self):
        return Vector2D(self.abscissa, self.ordinate * -1)

    # ваш код
